from typing import Type

from datetime import datetime

from beanie import (
    PydanticObjectId,
    Document,
)

from .update_by_id import update_by_id


async def soft_delete_by_id(
        document: Type[Document],
        id_: PydanticObjectId) -> Document:
    return await update_by_id(
        document=document,
        id_=id_,
        inputs={
            'is_deleted': True,
            'deleted_at': datetime.utcnow()
        },
    )
