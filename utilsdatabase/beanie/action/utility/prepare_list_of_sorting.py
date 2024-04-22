from typing import (
    Dict,
    List,
)

from beanie import SortDirection
from utilsdatabase.utilsdatabase.beanie.enum import EnumOrderBy

ASCENDING = SortDirection.ASCENDING
DESCENDING = SortDirection.DESCENDING


def prepare_list_of_sorting(order_by: Dict[str, EnumOrderBy] | None = None) -> List:
    list_of_sorting = list()
    for key, value in order_by.items():
        order = ASCENDING if value == EnumOrderBy.ascending else DESCENDING
        list_of_sorting.append((key, order))

    return list_of_sorting
