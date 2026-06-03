from usql.models.base import Model

from usql.fields.string import StringField
from usql.fields.integer import IntegerField

from usql.schema.builder import (
    SchemaBuilder
)


class Student(Model):

    name = StringField()

    age = IntegerField()


metadata, table = SchemaBuilder.build(
    Student
)

print(table)
print(table.columns.keys())