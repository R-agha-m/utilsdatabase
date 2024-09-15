from enum import Enum


class EnumOrderBy(str, Enum):
    ascending = "A"
    descending = "D"

    ASCENDING = "A"
    DESCENDING = "D"

    A = "A"
    D = "D"
