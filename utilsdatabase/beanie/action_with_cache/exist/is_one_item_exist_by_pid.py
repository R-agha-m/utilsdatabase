from typing import Type

from beanie import Document
from utilscommon.exception.project_base_exception import ProjectBaseException


async def is_one_item_exist_by_pid(
        document: Type[Document],
        pid: str,
        raise_on_absence: bool = False,
        exception_input: dict = dict(),  # noqa
) -> bool:
    result = await document.find_one(
        {'pid': pid},
        fetch_links=False,
    ).exists()

    if result:
        return True

    else:
        if raise_on_absence:
            raise ProjectBaseException(**exception_input)

        return False
