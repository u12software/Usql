from sqlalchemy import Integer

from usql.fields.base import Field


class IntegerField(Field):

    def to_sqlalchemy(self):

        return Integer