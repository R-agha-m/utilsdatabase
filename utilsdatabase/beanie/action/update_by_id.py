from typing import Type

from beanie import (
    PydanticObjectId,
    Document,
)

from .fetch_by_id import fetch_by_id


async def update_by_id(
        document: Type[Document],
        id_: PydanticObjectId,
        inputs: dict,
) -> Document:
    obj = await fetch_by_id(
        document=document,
        id_=id_,
    )

    for attr, value in inputs.items():
        setattr(obj, attr, value)

    await obj.save()

    return obj
