from typing import Type

from beanie import (
    PydanticObjectId,
    Document,
    UpdateResponse,

)


async def update_one_by_id_no_return(
        document: Type[Document],
        id_: PydanticObjectId,
        inputs: dict,
) -> UpdateResponse:
    """This function do not return the updated obj. Only update result will be returned!"""
    return await document.find_one({'id': id_}).update({"$set": inputs})
