from typing import Type

from beanie import (
    Document,
    UpdateResponse,

)


async def update_one_by_pid_no_return(
        document: Type[Document],
        pid: int,
        inputs: dict,
) -> UpdateResponse:
    """This function do not return the updated obj. Only update result will be returned!"""
    return await document.find_one({'pid': pid}).update({"$set": inputs})
