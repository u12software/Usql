from sqlalchemy import Table

class TableRegistry:

    _tables: dict[str, Table] = {}

    @classmethod
    def register(
        cls,
        model_name,
        table
    ):
        cls._tables[model_name] = table

    @classmethod
    def get(cls, model_name: str) -> Table:

        table = cls._tables.get(model_name)

        if table is None:

            raise ValueError(
                f"Table '{model_name}' non enregistrée"
            )

        return table

    @classmethod
    def all(cls):
        return cls._tables