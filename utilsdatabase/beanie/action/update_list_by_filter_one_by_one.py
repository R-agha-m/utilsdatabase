from typing import (
    Type,
    Dict,
)

from beanie import Document

from ..enum import EnumOrderBy
from .fetch_list_by_filter import fetch_list_by_filter


async def update_list_by_filter_one_by_one(
        document: Type[Document],
        filter_: Dict,
        inputs: dict,
        current_page: int = 1,
        page_size: int = 10,
        order_by: Dict[str, EnumOrderBy] | None = None,
        fetch_links: bool = False,
) -> list[Document]:
    objs = await fetch_list_by_filter(
        document=document,
        filter_=filter_,
        aggregate=None,
        current_page=current_page,
        page_size=page_size,
        order_by=order_by,
        project_model=None,
        fetch_links=fetch_links,
    )

    for obj in objs:
        for attr, value in inputs.items():
            setattr(obj, attr, value)

        await obj.save()

    return objs
