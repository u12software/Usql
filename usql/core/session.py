from sqlalchemy.orm import sessionmaker


class SessionFactory:

    @staticmethod
    def create(engine):

        return sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False
        )