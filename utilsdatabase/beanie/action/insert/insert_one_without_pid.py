from typing import Type

from beanie import Document


async def insert_one_without_pid(
        document: Type[Document],
        inputs: dict,
) -> Type[Document] | Document:
    obj = document(**inputs)
    await obj.insert()
    return obj
