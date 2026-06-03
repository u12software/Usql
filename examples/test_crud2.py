from usql import Usql

from usql.models.base import Model

from usql.fields.string import StringField
from usql.fields.integer import IntegerField


class Student(Model):

    name = StringField()

    age = IntegerField()


db = Usql(
    engine="sqlite",
    database="school.db"
)

db.register(Student)

db.create_all()

print("FIRST")
print(Student.first())

print("LAST")
print(Student.last())

print("EXISTS")
print(Student.exists(id=1))

print("UPDATE")
Student.update(
    1,
    age=20
)

print(Student.get(id=1))

print("DELETE")
Student.delete(2)

print(Student.all())