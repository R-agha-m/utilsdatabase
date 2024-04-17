from typing import Type

from datetime import datetime

from beanie import (
    PydanticObjectId,
    Document,
)

from .fetch_by_id import fetch_by_id


async def hard_delete_by_id(
        document: Type[Document],
        id_: PydanticObjectId,
) -> None:
    obj = await fetch_by_id(
        document=document,
        id_=id_,
    )
    await obj.delete()
