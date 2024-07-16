from typing import Type

from beanie import Document


async def update_one_by_obj(
        obj: Type[Document] | Document,
        inputs: dict,
) -> Type[Document]:
    for attr, value in inputs.items():
        setattr(obj, attr, value)

    await obj.save()

    return obj
