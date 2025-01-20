from __future__ import annotations

from sqlalchemy import URL, create_engine, exc, text

from patchwork.common.utils.utils import mustache_render
from patchwork.logger import logger
from patchwork.step import Step, StepStatus
from patchwork.steps.CallSQL.typed import CallSQLInputs, CallSQLOutputs


class CallSQL(Step, input_class=CallSQLInputs, output_class=CallSQLOutputs):
    def __init__(self, inputs: dict):
        super().__init__(inputs)
        query_template_data = inputs.get("db_query_template_values", {})
        self.query = mustache_render(inputs["db_query"], query_template_data)
        self.__build_engine(inputs)

    def __build_engine(self, inputs: dict):
        dialect = inputs["db_dialect"]
        driver = inputs.get("db_driver")
        dialect_plus_driver = f"{dialect}+{driver}" if driver is not None else dialect
        kwargs = dict(
            username=inputs["db_username"],
            host=inputs.get("db_host", "localhost"),
            port=inputs.get("db_port", 5432),
        )
        if inputs.get("db_password") is not None:
            kwargs["password"] = inputs.get("db_password")
        if inputs.get("db_name") is not None:
            kwargs["database"] = inputs.get("db_name")
        if inputs.get("db_params") is not None:
            kwargs["query"] = inputs.get("db_params")
        connection_url = URL.create(
            dialect_plus_driver,
            **kwargs,
        )

        connect_args = None
        if inputs.get("db_driver_args") is not None:
            connect_args = inputs.get("db_driver_args")

        self.engine = create_engine(connection_url, connect_args=connect_args)
        with self.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return self.engine

    def run(self) -> dict:
        try:
            rv = []
            with self.engine.begin() as conn:
                cursor = conn.execute(text(self.query))
                for row in cursor:
                    result = row._asdict()
                    rv.append(result)
            logger.info(f"Retrieved {len(rv)} rows!")
            return dict(results=rv)
        except exc.InvalidRequestError as e:
            self.set_status(StepStatus.FAILED, f"`{self.query}` failed with message:\n{e}")
            return dict(results=[])
