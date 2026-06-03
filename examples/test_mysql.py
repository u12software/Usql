from usql import Usql


db = Usql(
    engine="mysql",
    database="school",
    user="root",
    password="1234",
    host="localhost"
)

print(
    db.is_connected()
)