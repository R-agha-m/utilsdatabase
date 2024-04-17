from typing import (
    Type,
    Dict,
)

from beanie import Document


async def hard_delete_by_filter(
        document: Type[Document],
        filter_: Dict,
        fetch_links: bool = False,
) -> None:
    return await document.find_one(
        filter_,
        fetch_links=fetch_links,
    ).delete()
