from typing import (
    Type,
    Dict,
)

from datetime import datetime

from beanie import Document

from .update_one_by_filter import update_one_by_filter


async def soft_delete_by_filter(
        document: Type[Document],
        filter_: Dict,
        fetch_links: bool = False,
) -> Document:
    return await update_one_by_filter(
        document=document,
        filter_=filter_,
        inputs={
            'is_deleted': True,
            'deleted_at': datetime.utcnow()
        },
        fetch_links=fetch_links,
    )
