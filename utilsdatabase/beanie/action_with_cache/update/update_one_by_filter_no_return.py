from typing import (
    Type,
    Dict,
)

from beanie import Document


async def update_one_by_filter_no_return(
        document: Type[Document],
        filter_: Dict,
        inputs: dict,
        fetch_links: bool = False,
) -> Document:
    """This function do not return the updated obj. Only update result will be returned!"""
    return await document.find_one(
        filter_,
        fetch_links=fetch_links,
    ).update({"$set": inputs})
