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
from utilsdatabase.utilsdatabase.beanie.enum import EnumOrderBy
from utilsdatabase.utilsdatabase.beanie.action.utility.prepare_list_of_sorting import prepare_list_of_sorting
from utilsdatabase.utilsdatabase.beanie.action.utility.prepare_skip_limit_for_aggregation import \
    prepare_skip_limit_for_aggregation


async def fetch_list_by_aggregation_with_pagination(
        document: Type[Document],
        aggregation: Optional[List[Dict]] = None,
        first_filter: dict = None,
        last_filter: dict = None,
        sort: dict[str, SortDirection] = None,
        order_by: Dict[str, EnumOrderBy] | None = None,
        current_page: int = 1,
        page_size: int = 10,
        project_model: Optional[Type[BaseModel]] = None,
) -> Dict:
    if order_by:
        order_by = {key.replace("__", "."): value for key, value in order_by.items()}
        sort = dict(prepare_list_of_sorting(order_by=order_by))

    skip_limit_list = prepare_skip_limit_for_aggregation(
        current_page=current_page,
        page_size=page_size,
    )

    _aggregation_for_result = list()
    _aggregation_for_count = list()

    if first_filter:
        _aggregation_for_result.append({'$match': first_filter})
        _aggregation_for_count.append({'$match': first_filter})

    if aggregation:
        _aggregation_for_result.extend(aggregation)
        _aggregation_for_count.extend(aggregation)

    if last_filter:
        _aggregation_for_result.append({'$match': last_filter})
        _aggregation_for_count.append({'$match': last_filter})

    if sort:
        _aggregation_for_result.append({'$sort': sort})

    if skip_limit_list:
        _aggregation_for_result.extend(skip_limit_list)

    _aggregation_for_count.append({'$count': 'count'})

    result = await document.find({}).aggregate(_aggregation_for_result).to_list()
    count = await document.find({}).aggregate(_aggregation_for_count).to_list()
    count = 0 if not count else count[0]['count']

    return {
        "pagination": {
            "total": count,
            "current": current_page,
            "page_size": page_size or count
        },
        "data": result
    }

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
