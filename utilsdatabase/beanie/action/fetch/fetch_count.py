from typing import (
    Type,
    Dict,
)

from beanie import Document


async def fetch_count(
        document: Type[Document],
        filter_: Dict,
) -> int:

    return await document.find(filter_).count()
