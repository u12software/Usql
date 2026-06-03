from usql.schema.builder import SchemaBuilder
from usql.schema.registry import TableRegistry


class SchemaManager:

    @staticmethod
    def register(model):

        metadata, table = (
            SchemaBuilder.build(model)
        )

        TableRegistry.register(
            model.__name__,
            table
        )

        return metadata, table