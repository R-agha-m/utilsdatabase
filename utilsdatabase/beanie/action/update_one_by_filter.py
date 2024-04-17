from typing import (
    Type,
    Dict,
)

from beanie import Document

from .fetch_one_by_filter import fetch_one_by_filter


async def update_one_by_filter(
        document: Type[Document],
        filter_: Dict,
        inputs: dict,
        fetch_links: bool = False,
) -> Document:
    obj = await fetch_one_by_filter(
        document=document,
        filter_=filter_,
        fetch_links=fetch_links,
    )

    for attr, value in inputs.items():
        setattr(obj, attr, value)

    await obj.save()

    return obj
