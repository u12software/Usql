from usql import Usql


db = Usql(
    engine="postgresql",
    database="school",
    user="postgres",
    password="postgres",
    host="localhost"
)

print(
    db.is_connected()
)