from typing import Type

from beanie import (
    PydanticObjectId,
    Document,
)


async def delete_one_by_id(
        document: Type[Document],
        id_: PydanticObjectId,
) -> None:
    return await document.find_one(
        {"id": id_},
    ).delete()
