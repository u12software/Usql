from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import update
from sqlalchemy import delete

from usql.core.context import ORMContext
from usql.schema.registry import TableRegistry
from usql.query.manager import QueryManager


class ModelManager:

    @staticmethod
    def create(model, **kwargs):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = insert(table).values(
            **kwargs
        )

        session.execute(stmt)

        session.commit()

        session.close()

    @staticmethod
    def all(model):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = select(table)

        rows = session.execute(
            stmt
        ).mappings().all()

        session.close()

        return [
            dict(row)
            for row in rows
        ]
    
    @staticmethod
    def get(model, **filters):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = select(table)

        for key, value in filters.items():

            stmt = stmt.where(
                table.c[key] == value
            )

        row = session.execute(
            stmt
        ).mappings().first()

        session.close()

        if row is None:
            return None

        return dict(row)
    
    @staticmethod
    def filter(model, **filters):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = select(table)

        stmt = QueryManager.apply_filters(
            stmt,
            table,
            filters
        )

        rows = session.execute(
            stmt
        ).mappings().all()

        session.close()

        return [
            dict(row)
            for row in rows
        ]
    
    @staticmethod
    def count(model):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = select(
            func.count()
        ).select_from(table)

        total = session.execute(
            stmt
        ).scalar()

        session.close()

        return total

    @staticmethod
    def first(model):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = select(table)

        row = session.execute(
            stmt
        ).mappings().first()

        session.close()

        if row is None:
            return None

        return dict(row)

    @staticmethod
    def last(model):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = (
            select(table)
            .order_by(
                table.c.id.desc()
            )
        )

        row = session.execute(
            stmt
        ).mappings().first()

        session.close()

        if row is None:
            return None

        return dict(row)
    
    @staticmethod
    def exists(model, **filters):

        result = ModelManager.get(
            model,
            **filters
        )

        return result is not None

    @staticmethod
    def update(model, id, **values):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = (
            update(table)
            .where(
                table.c.id == id
            )
            .values(**values)
        )

        session.execute(stmt)

        session.commit()

        session.close()
    
    @staticmethod
    def delete(model, id):

        table = TableRegistry.get(
            model.__name__
        )

        session = ORMContext.session_factory()

        stmt = delete(table).where(
            table.c.id == id
        )

        session.execute(stmt)

        session.commit()

        session.close()