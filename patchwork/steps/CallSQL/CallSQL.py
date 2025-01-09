from __future__ import annotations

from sqlalchemy import URL, create_engine, exc, text

from patchwork.common.utils.utils import mustache_render
from patchwork.step import Step, StepStatus
from patchwork.steps.CallSQL.typed import CallSQLInputs, CallSQLOutputs


class CallSQL(Step, input_class=CallSQLInputs, output_class=CallSQLOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        query_template_data = inputs.get("query_template_values", {})
        self.query = mustache_render(inputs["query"], query_template_data)
        self.__build_engine(inputs)

    def __build_engine(self, inputs: dict):
        dialect = inputs["dialect"]
        driver = inputs.get("driver")
        dialect_plus_driver = f"{dialect}+{driver}" if driver is not None else dialect
        kwargs = dict(
            username=inputs["username"],
            host=inputs.get("host", "localhost"),
            port=inputs.get("port", 5432),
        )
        if inputs.get("password") is not None:
            kwargs["password"] = inputs.get("password")
        connection_url = URL.create(
            dialect_plus_driver,
            **kwargs,
        )
        self.engine = create_engine(connection_url)
        with self.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return self.engine

    def run(self) -> dict:
        try:
            with self.engine.begin() as conn:
                cursor = conn.execute(text(self.query))
                result = cursor.fetchall()
            return dict(result=result)
        except exc.InvalidRequestError as e:
            self.set_status(StepStatus.FAILED, f"`{self.query}` failed with message:\n{e}")
            return dict(result=[])
