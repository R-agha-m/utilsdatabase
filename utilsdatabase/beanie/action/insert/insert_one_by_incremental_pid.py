from typing import Type

from beanie import Document

from .utility import calculate_incremental_pid


async def insert_one_by_incremental_pid(
        document: Type[Document],
        inputs: dict,
) -> Type[Document] | Document:
    inputs_with_pid = {
        'pid': await calculate_incremental_pid(document=document),
        **inputs,
    }
    obj = document(**inputs_with_pid)
    await obj.insert()
    return obj
