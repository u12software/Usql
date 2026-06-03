from sqlalchemy import String

from usql.fields.base import Field


class StringField(Field):

    def __init__(
        self,
        length=255,
        **kwargs
    ):

        super().__init__(**kwargs)

        self.length = length

    def to_sqlalchemy(self):

        return String(self.length)