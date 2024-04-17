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


async def fetch_list_by_filter_with_pagination(
        document: Type[Document],
        filter_: Dict,
        current_page: int = 1,
        page_size: int = 10,
        order_by: Dict[str, EnumOrderBy] | None = None,
        project_model: Optional[Type[BaseModel]] = None,
        fetch_links: bool = False,
        aggregate: Optional[list] = None,
        aggregate_count: Optional[list] = None,
) -> dict:
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

    result = await query.to_list()

    if aggregate:
        count = await document.find({}).aggregate(aggregate_count)

    else:
        count = await query.count()

    return {
        "pagination": {
            "total": count,
            "current": current_page,
            "page_size": page_size
        },
        "data": result
    }