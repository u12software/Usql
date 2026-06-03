from sqlalchemy import select

from usql.core.context import ORMContext
from usql.schema.registry import TableRegistry
from usql.query.manager import QueryManager


class QueryBuilder:

    @staticmethod
    def execute(queryset):

        table = TableRegistry.get(
            queryset.model.__name__
        )

        stmt = select(table)

        stmt = QueryManager.apply_filters(
            stmt,
            table,
            queryset.filters
        )

        session = ORMContext.session_factory()

        rows = session.execute(
            stmt
        ).mappings().all()

        session.close()

        return [
            dict(row)
            for row in rows
        ]