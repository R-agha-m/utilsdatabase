from typing import Type

from beanie import Document
from utilscommon.exception.project_base_exception import ProjectBaseException


async def is_one_item_absent_by_pid(
        document: Type[Document],
        pid: int | str,
        raise_on_existence: bool = False,
        exception_input: dict = dict(),  # noqa
) -> bool:
    result = await document.find_one(
        {'pid': pid},
        fetch_links=False,
    ).exists()

    if result:
        if raise_on_existence:
            raise ProjectBaseException(**exception_input)

        return False

    else:
        return True
