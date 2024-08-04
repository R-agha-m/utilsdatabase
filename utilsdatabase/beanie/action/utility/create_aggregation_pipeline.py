from typing import (
    Collection,
    Type,
    Literal,
    Dict,
)

from pydantic import BaseModel


def create_aggregation_pipeline(
        attributes: tuple[tuple[str, Type[BaseModel]], ...],
        final_projection: Type[BaseModel] | dict[str, Literal[0, 1]] = None
) -> list[dict]:
    aggregation_pipeline = list()

    for attribute_name, projection in attributes:
        projection_fields = prepare_projection_fields(projection=projection)

        aggregation_pipeline.extend(
            [
                {
                    '$lookup': {
                        'from': attribute_name,
                        'localField': f"{attribute_name}_pid",
                        'foreignField': "pid",
                        'as': f"{attribute_name}_obj",
                        'pipeline': [
                            {
                                '$project': projection_fields
                            }
                        ]
                    }
                },
                {
                    '$unwind': {
                        'path': f"${attribute_name}_obj",
                        'preserveNullAndEmptyArrays': True
                    }
                }
            ]
        )

    aggregation_pipeline.append({"$project": prepare_projection_fields(projection=final_projection)})
    return aggregation_pipeline


def prepare_projection_fields(
        projection: Type[BaseModel]
                    | Dict[str | Literal[0, 1], ...]
                    | None
) -> Dict[str | Literal[0, 1], ...]:
    if isinstance(projection, dict):
        return projection

    elif issubclass(projection,BaseModel):
        return {
            '_id': 0,
            **{i: 1 for i in projection.model_fields.keys()}
        }
    return {"_id": 0}

#
# AGGREGATION_PIPELINE_EXAMPLE = [
#     {
#         '$lookup': {
#             'from': "server",
#             'localField': "server_pid",
#             'foreignField': "pid",
#             'as': "server_obj",
#             'pipeline': [
#                 {
#                     '$project': {
#                         '_id': 0,
#                         **{i: 1 for i in ProxyModelFetchByPidResponse.model_fields.keys()}
#                     }
#                 }
#             ]
#         }
#     },
#     {
#         '$unwind': {
#             'path': "$server_obj",
#             'preserveNullAndEmptyArrays': True
#         }
#     },
#     {
#         '$lookup': {
#             'from': "proxy",
#             'localField': "proxy_pid",
#             'foreignField': "pid",
#             'as': "proxy_obj",
#             'pipeline': [
#                 {
#                     '$project': {
#                         '_id': 0,
#                         **{i: 1 for i in ProxyModelFetchByPidResponse.model_fields.keys()}
#                     }
#                 }
#             ]
#         }
#     },
#     {
#         '$unwind': {
#             'path': "$proxy_obj",
#             'preserveNullAndEmptyArrays': True
#         }
#     },
#     {
#         '$project': {
#             "_id": 0
#         }
#     }
# ]
