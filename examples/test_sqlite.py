from usql import Usql


db = Usql(
    engine="sqlite",
    database="school.db"
)

print(
    "Connexion :",
    db.is_connected()
)