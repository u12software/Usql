from typing import Optional


class PostgreSQLAdapter:

    @staticmethod
    def build_url(
        database: str,
        user: Optional[str],
        password: Optional[str],
        host: str,
        port: int
    ) -> str:

        if not user:
            raise ValueError(
                "PostgreSQL nécessite un utilisateur"
            )

        if not password:
            raise ValueError(
                "PostgreSQL nécessite un mot de passe"
            )

        return (
            f"postgresql+psycopg2://"
            f"{user}:{password}@"
            f"{host}:{port}/"
            f"{database}"
        )