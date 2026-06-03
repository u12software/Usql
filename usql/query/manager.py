from sqlalchemy import select

from usql.query.filters import QueryFilter


class QueryManager:

    @staticmethod
    def apply_filters(
        stmt,
        table,
        filters
    ):

        for key, value in filters.items():

            field, operator = (
                QueryFilter.parse(key)
            )

            column = table.c[field]

            if operator == "eq":

                stmt = stmt.where(
                    column == value
                )

            elif operator == "gt":

                stmt = stmt.where(
                    column > value
                )

            elif operator == "gte":

                stmt = stmt.where(
                    column >= value
                )

            elif operator == "lt":

                stmt = stmt.where(
                    column < value
                )

            elif operator == "lte":

                stmt = stmt.where(
                    column <= value
                )
            
            elif operator == "in":

                stmt = stmt.where(
                    column.in_(value)
                )

            elif operator == "not":

                stmt = stmt.where(
                    column != value
                )

            elif operator == "contains":

                stmt = stmt.where(
                    column.contains(value)
                )

            elif operator == "startswith":

                stmt = stmt.where(
                    column.startswith(value)
                )

            elif operator == "endswith":

                stmt = stmt.where(
                    column.endswith(value)
                )

        return stmt