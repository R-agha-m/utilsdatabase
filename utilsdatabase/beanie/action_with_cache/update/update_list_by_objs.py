from typing import (
    Type,
    List,
)

from beanie import Document


async def update_list_by_objs(
        objs: List[Type[Document]],
        inputs: dict,
) -> List[Type[Document]]:
    for obj in objs:
        for attr, value in inputs.items():
            setattr(obj, attr, value)

        await obj.save()

    return objs
