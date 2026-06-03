class SQLiteAdapter:

    @staticmethod
    def build_url(database: str) -> str:
        return f"sqlite:///{database}"