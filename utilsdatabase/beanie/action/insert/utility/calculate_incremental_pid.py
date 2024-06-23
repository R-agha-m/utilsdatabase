from typing import Type

from beanie import (
    Document,
    SortDirection,
)

sort = [("pid", SortDirection.DESCENDING)]


async def calculate_incremental_pid(document: Type[Document]) -> int:
    result = await document.find_many(
        {},
        sort=sort,
    ).first_or_none()

    if result is None:
        pid = 1
    else:
        pid = result.pid + 1

    return pid
