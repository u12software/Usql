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


Student.create(
    name="Jean",
    age=15
)

Student.create(
    name="Marie",
    age=17
)


print(
    Student.all()
)