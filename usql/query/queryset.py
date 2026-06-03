class QuerySet:

    def __init__(self, model):

        self.model = model

        self.filters = {}

        self.ordering = None

        self.limit_value = None

        self.offset_value = None