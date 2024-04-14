from typing import (
    Dict,
    List,
)

from pymongo import ASCENDING, DESCENDING

from utilsdatabase.utilsdatabase.beanie.enum import EnumOrderBy


def prepare_list_of_sorting(order_by: Dict[str, EnumOrderBy] | None = None, ) -> List:
    list_of_sorting = list()
    if order_by:
        for key, value in order_by.items():
            order = ASCENDING if value == EnumOrderBy.ascending else DESCENDING
            list_of_sorting.append((key, order))

    return list_of_sorting
