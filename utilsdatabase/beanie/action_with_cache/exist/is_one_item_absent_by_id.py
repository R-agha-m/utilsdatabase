from typing import Type

from beanie import (
    Document,
    PydanticObjectId,
)
from utilscommon.utilscommon.exception.project_base_exception import ProjectBaseException


async def is_one_item_absent_by_id(
        document: Type[Document],
        id_: PydanticObjectId,
        raise_on_existence: bool = False,
        exception_input: dict = dict(),  # noqa
) -> bool:
    result = await document.find_one(
        {'id': id_},
        fetch_links=False,
    ).exists()

    if result:
        if raise_on_existence:
            raise ProjectBaseException(**exception_input)

        return False

    else:
        return True
