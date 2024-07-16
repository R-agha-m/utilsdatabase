from typing import Type

from beanie import (
    PydanticObjectId,
    Document,
)


async def update_one_by_id_with_return(
        document: Type[Document],
        id_: PydanticObjectId,
        inputs: dict,
) -> Document:
    obj = await document.get(document_id=id_)

    for attr, value in inputs.items():
        setattr(obj, attr, value)

    await obj.save()

    return obj
