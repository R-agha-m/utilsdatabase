from typing import (
    List,
    Tuple,
    Type,
    Dict,
    Optional,
)

from beanie import (
    Document,
    SortDirection,
)
from pydantic import BaseModel

from utilsdatabase.beanie.enum import EnumOrderBy
from utilsdatabase.beanie.action.utility.prepare_list_of_sorting import prepare_list_of_sorting
from utilsdatabase.beanie.action.utility.prepare_skip_limit import prepare_skip_limit


async def fetch_list_by_filter(
        document: Type[Document],
        filter_: Dict,
        current_page: int = 1,
        page_size: int = 10,
        order_by: Dict[str, EnumOrderBy] | None = None,
        project_model: Optional[Type[BaseModel]] = None,
        sort: List[Tuple[str, SortDirection]] = None,
        fetch_links: bool = False,
) -> List[Document | Dict]:
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

    return await query.to_list()
