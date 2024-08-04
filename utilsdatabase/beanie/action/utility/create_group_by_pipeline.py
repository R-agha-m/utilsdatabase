from typing import (
    List,
    Dict,
)

DATETIME_BY_X_FORMAT = {
    "_by_year": "%Y",
    '_by_month': "%m",
    '_by_day': "%d",
    '_by_hour': "%H",
    '_by_minute': "%M",
    '_by_second': "%S",

    '_by_year_month': "%Y-%m",
    '_by_year_month_day': "%Y-%m-%d",
    '_by_year_month_day_hour': "%Y-%m-%d %H",
    '_by_year_month_day_hour_minute': "%Y-%m-%d %H:%M",
    '_by_year_month_day_hour_minute_second': "%Y-%m-%d %H:%M:%S",
}


def create_group_by_pipeline(
        group_by_on: list[str]
) -> List[Dict]:
    aggregation_pipeline = list()

    add_field = dict()
    group_id = dict()

    for field_alias_name in group_by_on:
        field_real_name = field_alias_name.replace("__", ".")

        if field_real_name.endswith(tuple(DATETIME_BY_X_FORMAT.keys())):
            for datetime_key, datetime_value in DATETIME_BY_X_FORMAT.items():

                if field_real_name.endswith(datetime_key):
                    field_alias_name = field_alias_name.replace(datetime_key, "")
                    field_real_name = field_real_name.replace(datetime_key, "")

                    add_field[field_alias_name] = {
                        "$dateToString": {
                            "format": datetime_value,
                            "date": f"${field_real_name}"
                        }
                    }

                    field_real_name = field_alias_name
                    break

        group_id[field_alias_name] = f"${field_real_name}"

    if add_field:
        aggregation_pipeline.append({'$addFields': add_field})

    aggregation_pipeline.append(
        {
            '$group': {
                '_id': group_id,
                'count': {'$sum': 1}
            }
        },
    )

    return aggregation_pipeline
