from typing import Type

from beanie import (
    Document,
    SortDirection,
)

sort = [("public_id", SortDirection.DESCENDING)]


async def calculate_public_id(document: Type[Document]) -> int:
    result = await document.find_many(
        {},
        sort=sort,
    ).first_or_none()

    if result is None:
        public_id = 1
    else:
        public_id = result.public_id + 1

    return public_id
