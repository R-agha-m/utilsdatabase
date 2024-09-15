from typing import Type

from beanie import Document


async def update_one_by_pid_with_return(
        document: Type[Document],
        pid: str,
        inputs: dict,
        fetch_links: bool = False,
) -> Document:
    obj = await document.find_one(
        {'pid': pid},
        projection_model=None,
        fetch_links=fetch_links,
        limit=1,
        sort=None,
    )

    for attr, value in inputs.items():
        setattr(obj, attr, value)

    await obj.save()

    return obj
