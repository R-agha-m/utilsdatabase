from typing import Type

from beanie import Document


async def insert(
        document: Type[Document],
        inputs: dict,
) -> Document:
    obj = document(**inputs)
    await obj.insert()
    return obj
