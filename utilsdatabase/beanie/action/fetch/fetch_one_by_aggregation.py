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

from ...enum import EnumOrderBy
from ..utility import (
    prepare_list_of_sorting,
    prepare_skip_limit_for_aggregation,
)


async def fetch_one_by_aggregation(
        document: Type[Document],
        aggregation: Optional[List[Dict]] = None,
        first_filter: dict = None,
        last_filter: dict = None,
        project_model: Optional[Type[BaseModel]] = None,
) -> Dict:
    _aggregation = list()

    if first_filter:
        _aggregation.append({'$match': first_filter})

    if aggregation:
        _aggregation.extend(aggregation)

    if last_filter:
        _aggregation.append({'$match': last_filter})

    results = await document.find({}).aggregate(_aggregation).to_list()
    return results[0]
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
# ]
