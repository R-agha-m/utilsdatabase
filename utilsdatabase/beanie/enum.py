from enum import Enum


class EnumOrderBy(str, Enum):
    ascending = "ascend"
    descending = "descend"
