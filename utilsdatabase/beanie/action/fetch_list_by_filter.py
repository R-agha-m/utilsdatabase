from typing import (
    List,
    Type,
    Dict,
    Optional,
)

from beanie import Document
from pydantic import BaseModel

from ..enum import EnumOrderBy
from .prepare_list_of_sorting import prepare_list_of_sorting
from .prepare_skip_limit import prepare_skip_limit


async def fetch_list_by_filter(
        document: Type[Document],
        filter_: Dict,
        aggregate: Optional[List[Dict]] = None,
        current_page: int = 1,
        page_size: int = 10,
        order_by: Dict[str, EnumOrderBy] | None = None,
        project_model: Optional[Type[BaseModel]] = None,
        fetch_links: bool = False,
) -> List[Document | Dict]:
    list_of_sorting = prepare_list_of_sorting(order_by=order_by)

    skip_limit_dictionary = prepare_skip_limit(
        current_page=current_page,
        page_size=page_size,
    )

    query = document.find(
        filter_,
        projection_model=project_model,
        **skip_limit_dictionary,
        sort=list_of_sorting,
        fetch_links=fetch_links,
    )

    if aggregate:
        query = query.aggregate(aggregate)

    return await query.to_list()
