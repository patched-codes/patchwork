from __future__ import annotations

from sqlalchemy import URL, create_engine, exc, text

from patchwork.common.utils.input_parsing import parse_to_dict
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
            username=inputs.get("db_username"),
            host=inputs.get("db_host", "localhost"),
            port=inputs.get("db_port", 5432),
            password=inputs.get("db_password"),
            database=inputs.get("db_database"),
            query=parse_to_dict(inputs.get("db_params")),
        )
        connection_url = URL.create(
            dialect_plus_driver,
            **{k: v for k, v in kwargs.items() if v is not None},
        )

        connect_args = dict()
        if inputs.get("db_driver_args") is not None:
            connect_args = parse_to_dict(inputs.get("db_driver_args"))

        self.engine = create_engine(connection_url, connect_args=connect_args)
        with self.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return self.engine

    def run(self) -> dict:
        try:
            rv = []
            with self.engine.begin() as conn:
                cursor = conn.exec_driver_sql(self.query)
                for row in cursor:
                    result = row._asdict()
                    rv.append(result)
            logger.info(f"Retrieved {len(rv)} rows!")
            return dict(results=rv)
        except exc.InvalidRequestError as e:
            self.set_status(StepStatus.FAILED, f"`{self.query}` failed with message:\n{e}")
            return dict(results=[])
