from typing import (
    Type,
    Dict,
    Optional,
)

from beanie import Document
from pydantic import BaseModel


async def fetch_one_by_filter(
        document: Type[Document],
        filter_: Dict,
        project_model: Optional[Type[BaseModel]] = None,
        fetch_links: bool = False,
) -> Document | Dict:
    return document.find_one(  # noqa
        filter_,
        projection_model=project_model,
        fetch_links=fetch_links,
    )
