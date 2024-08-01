from typing import (
    List,
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
from utilsdatabase.beanie.action.utility.prepare_skip_limit_for_aggregation import prepare_skip_limit_for_aggregation


async def fetch_list_by_aggregation(
        document: Type[Document],
        aggregation: Optional[List[Dict]] = None,
        first_filter: dict = None,
        last_filter: dict = None,
        sort: dict[str, SortDirection] = None,
        order_by: Dict[str, EnumOrderBy] | None = None,
        current_page: int = 1,
        page_size: int = 10,
        project_model: Optional[Type[BaseModel]] = None,
) -> List[Document | Dict]:
    if order_by:
        sort = dict(prepare_list_of_sorting(order_by=order_by))

    skip_limit_list = prepare_skip_limit_for_aggregation(
        current_page=current_page,
        page_size=page_size,
    )

    _aggregation = list()

    if first_filter:
        _aggregation.append({'$match': first_filter})

    if aggregation:
        _aggregation.extend(aggregation)

    if last_filter:
        _aggregation.append({'$match': last_filter})

    if sort:
        _aggregation.append({'$sort': sort})

    if skip_limit_list:
        _aggregation.extend(skip_limit_list)

    return await document.find({}).aggregate(_aggregation).to_list()

#  Aggregation example:
# [
#   {
#     $match: {
#       user_pid: 1
#     }
#   },
#   {
#     $lookup: {
#       from: "subject",
#       localField: "subject_pid",
#       foreignField: "pid",
#       as: "subject_obj"
#     }
#   },
#   {
#     $unwind: {
#       path: "$subject_obj",
#       preserveNullAndEmptyArrays: true
#     }
#   },
#   {
#     $lookup: {
#       from: "organization",
#       localField: "subject_pid",
#       foreignField: "pid",
#       as: "organization_obj"
#     }
#   },
#   {
#     $unwind: {
#       path: "$organization_obj",
#       preserveNullAndEmptyArrays: true
#     }
#   },
#   {
#     $lookup: {
#       from: "main_file",
#       localField: "main_file_pid",
#       foreignField: "pid",
#       as: "main_file_obj"
#     }
#   },
#   {
#     $unwind: {
#       path: "$main_file_obj",
#       preserveNullAndEmptyArrays: true
#     }
#   },
#       {
#     $match: {
#        "main_file_obj.file_extension": 'PDF'
#     }
#       },
#   {
#     $sort: {
#       // title: +1,
#       // "subject_obj.name_farsi": -1,
#       //  "organization_obj.name_farsi": -1,
#       "main_file_obj.file_extension": -1
#     }
#   },
#
#   {
#     $count: 'count'
#   }
#   // {
#   //   $skip: 2
#   // },
#   // {
#   //   $limit: 1
#   // }
# ]
