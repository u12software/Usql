from typing import Optional


class MySQLAdapter:

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
                "MySQL nécessite un utilisateur"
            )

        if not password:
            raise ValueError(
                "MySQL nécessite un mot de passe"
            )

        return (
            f"mysql+pymysql://"
            f"{user}:{password}@"
            f"{host}:{port}/"
            f"{database}"
        )