from typing import Any

from sqlalchemy import (
    Table,
    Column,
    MetaData,
    Integer
)

from usql.fields.string import StringField
from usql.fields.integer import IntegerField


class SchemaBuilder:

    @staticmethod
    def build(model):

        metadata = MetaData()

        columns: list[Any] = [
            Column(
                "id",
                Integer,
                primary_key=True
            )
        ]

        for field_name, field in model._fields.items():

            if isinstance(field, StringField):

                columns.append(
                    Column(
                        field_name,
                        field.to_sqlalchemy()
                    )
                )

            elif isinstance(field, IntegerField):

                columns.append(
                    Column(
                        field_name,
                        field.to_sqlalchemy()
                    )
                )

        table = Table(
            model.__name__.lower(),
            metadata,
            *columns
        )

        return metadata, table