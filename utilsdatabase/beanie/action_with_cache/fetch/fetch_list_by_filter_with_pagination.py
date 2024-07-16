from typing import (
    Type,
    Tuple,
    List,
    Dict,
    Optional,
)

from beanie import (
    Document,
    SortDirection,
)
from pydantic import BaseModel

from utilsdatabase.utilsdatabase.beanie.enum import EnumOrderBy
from utilsdatabase.utilsdatabase.beanie.action.utility.prepare_list_of_sorting import prepare_list_of_sorting
from utilsdatabase.utilsdatabase.beanie.action.utility.prepare_skip_limit import prepare_skip_limit


async def fetch_list_by_filter_with_pagination(
        document: Type[Document],
        filter_: Dict,
        current_page: int = 1,
        page_size: int = 10,
        order_by: Dict[str, EnumOrderBy] | None = None,
        sort: List[Tuple[str, SortDirection]] = None,
        project_model: Optional[Type[BaseModel]] = None,
        fetch_links: bool = False,
) -> dict:
    if order_by:
        sort = prepare_list_of_sorting(order_by=order_by)

    skip_limit_dictionary = prepare_skip_limit(
        current_page=current_page,
        page_size=page_size,
    )

    query = document.find(
        filter_,
        projection_model=project_model,
        **skip_limit_dictionary,
        sort=sort,
        fetch_links=fetch_links,
    )

    result = await query.to_list()
    count = await query.count()

    return {
        "pagination": {
            "total": count,
            "current": current_page,
            "page_size": page_size or count
        },
        "data": result
    }
