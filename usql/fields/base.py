class Field:

    def __init__(
        self,
        primary_key=False,
        nullable=True,
        default=None
    ):

        self.primary_key = primary_key
        self.nullable = nullable
        self.default = default

    def to_sqlalchemy(self):
        raise NotImplementedError