from typing import Type

from beanie import (
    PydanticObjectId,
    Document,
)


async def fetch_by_id(
        document: Type[Document],
        id_: PydanticObjectId,
) -> Document:
    return await document.get(document_id=id_)
