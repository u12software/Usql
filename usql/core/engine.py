from sqlalchemy import create_engine

from usql.adapters.sqlite import SQLiteAdapter
from usql.adapters.postgres import PostgreSQLAdapter
from usql.adapters.mysql import MySQLAdapter

from usql.utils.exceptions import AdapterError
from typing import Optional


class EngineFactory:

    @staticmethod
    def create(
        engine,
        database,
        user=None,
        password=None,
        host="localhost",
        port=None
    ):

        if engine == "sqlite":

            url = SQLiteAdapter.build_url(database)

        elif engine == "postgresql":

            url = PostgreSQLAdapter.build_url(
                database,
                user,
                password,
                host,
                port or 5433
            )

        elif engine == "mysql":

            url = MySQLAdapter.build_url(
                database,
                user,
                password,
                host,
                port or 3306
            )

        else:
            raise AdapterError(
                f"Engine '{engine}' non supporté"
            )

        return create_engine(url)