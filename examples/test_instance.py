from usql.models.base import Model

from usql.fields.string import StringField
from usql.fields.integer import IntegerField


class Student(Model):

    name = StringField()

    age = IntegerField()


student = Student(
    name="Jean",
    age=15
)

print(student.name)
print(student.age)

print(student.to_dict())