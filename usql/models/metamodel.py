from usql.models.registry import ModelRegistry
from usql.fields.base import Field


class MetaModel(type):

    def __new__(
        cls,
        name,
        bases,
        attrs
    ):

        fields = {}

        for key, value in list(attrs.items()):

            if isinstance(value, Field):

                fields[key] = value

        attrs["_fields"] = fields

        new_class = super().__new__(
            cls,
            name,
            bases,
            attrs
        )

        if name != "Model":

            ModelRegistry.register(
                new_class
            )

        return new_class