from typing import Type

from beanie import Document


async def delete_one_by_pid(
        document: Type[Document],
        pid: int,
) -> None:
    return await document.find_one(
        {"pid": pid},
    ).delete()
