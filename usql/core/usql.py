from sqlalchemy import text

from usql.core.engine import EngineFactory
from usql.core.session import SessionFactory

from usql.models.registry import (
    ModelRegistry
)

from usql.schema.manager import (
    SchemaManager
)
from usql.core.context import ORMContext

class Usql:

    def __init__(
        self,
        engine,
        database,
        user=None,
        password=None,
        host="localhost",
        port=None
    ):

        self.engine = EngineFactory.create(
            engine,
            database,
            user,
            password,
            host,
            port
        )

        self.session_factory = (
            SessionFactory.create(
                self.engine
            )
        )

        self.metadata = []
        ORMContext.engine = self.engine
        ORMContext.session_factory = self.session

    def session(self):

        return self.session_factory()

    def is_connected(self):

        try:

            with self.engine.connect() as conn:

                conn.execute(text("SELECT 1"))

            return True

        
        except Exception as e:
            import traceback

            print(type(e))
            print(repr(e))

            traceback.print_exc()

            return False
    
    def register(self, model):

        metadata, table = (
            SchemaManager.register(model)
        )

        self.metadata.append(
            metadata
        )
    
    def create_all(self):

        for metadata in self.metadata:

            metadata.create_all(
                self.engine
            )