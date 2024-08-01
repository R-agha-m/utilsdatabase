from typing import (
    Type,
    Dict,
    Optional,
    Union,
    List,
    Tuple,
)

from beanie import (
    Document,
    SortDirection,
)
from pydantic import BaseModel

from utilsdatabase.beanie.enum import EnumOrderBy
from utilsdatabase.beanie.action.utility.prepare_list_of_sorting import prepare_list_of_sorting


async def fetch_one_by_pid(
        document: Type[Document],
        pid: int,
        project_model: Optional[Type[BaseModel]] = None,
        fetch_links: bool = False,
        skip: Optional[int] = None,
        order_by: Dict[str, EnumOrderBy] | None = None,
        sort: Union[None, str, List[Tuple[str, SortDirection]]] = None,
) -> Document | None:
    if order_by:
        sort = prepare_list_of_sorting(order_by=order_by)

    return await document.find_many(
        {'pid': pid},
        projection_model=project_model,
        fetch_links=fetch_links,
        skip=skip,
        limit=1,
        sort=sort,
    ).first_or_none()
