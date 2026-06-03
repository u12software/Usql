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

print(
    Student.filter(age=15)
)