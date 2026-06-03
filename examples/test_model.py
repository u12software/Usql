from usql.models.base import Model

from usql.fields.string import StringField
from usql.fields.integer import IntegerField

from usql.models.registry import (
    ModelRegistry
)


class Student(Model):

    name = StringField()

    age = IntegerField()


print(ModelRegistry.all())
print(Student._fields)