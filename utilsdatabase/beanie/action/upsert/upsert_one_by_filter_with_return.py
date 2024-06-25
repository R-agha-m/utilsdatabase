from typing import (
    Type,
    Dict,
)

from beanie import Document


async def upsert_one_by_filter_with_return(
        document: Type[Document],
        filter_: Dict,
        inputs: dict,
        fetch_links: bool = False,
) -> Document:
    obj = await document.find_many(
        filter_,
        projection_model=None,
        fetch_links=fetch_links,
        skip=None,
        limit=1,
        sort=None,
    ).first_or_none()

    if obj:
        for attr, value in inputs.items():
            setattr(obj, attr, value)

        await obj.save()

        return obj
    else:

