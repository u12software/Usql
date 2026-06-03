class QueryFilter:

    @staticmethod
    def parse(key):

        if "__" not in key:

            return key, "eq"

        field, operator = key.split(
            "__",
            1
        )

        return field, operator