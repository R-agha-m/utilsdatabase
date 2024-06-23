from typing import Type

from pymongo.errors import DuplicateKeyError
from beanie import Document

from .utility import calculate_epoch_pid


async def insert_one_by_epoch_pid(
        document: Type[Document],
        inputs: dict,
) -> Type[Document] | Document:
    while True:
        try:
            inputs_with_pid = {
                'pid': calculate_epoch_pid(),
                **inputs,
            }
            obj = document(**inputs_with_pid)
            await obj.insert()
            return obj
        except DuplicateKeyError as e:
            if not getattr(e, 'details', None):
                raise

            if e.details.get('keyPattern') != {'pid': 1}:
                raise
