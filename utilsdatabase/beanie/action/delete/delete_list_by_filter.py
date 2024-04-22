from typing import (
    Type,
    Dict,
)

from beanie import Document


async def delete_list_by_filter(
        document: Type[Document],
        filter_: Dict,
        fetch_links: bool = False,
) -> None:
    return await document.find(
        filter_,
        fetch_links=fetch_links,
    ).delete()
