from typing import (
    List,
    Type,
    Dict,
    Optional,
)

from beanie import Document


async def fetch_list_by_aggregate(
        document: Type[Document],
        aggregate: Optional[List[Dict]] = None,
) -> List[Document | Dict]:
    return await document.find({}).aggregate(aggregate).to_list()
