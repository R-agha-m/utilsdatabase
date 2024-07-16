from typing import (
    Tuple,
    Dict,
)

from .prepare_filter import prepare_filter


def prepare_filter_for_aggregation(
        inputs: Dict,
        fields_names_for_regex: Tuple[str, ...] = tuple(),
        fields_names_for_range: Tuple[str, ...] = tuple(),
        fields_names_for_in: Tuple[str, ...] = tuple(),
        search_field_name: str = None,
        fields_names_for_search: Tuple[str, ...] = tuple(),
) -> tuple[dict, dict]:
    first_filter_inputs = dict()
    last_filter_inputs = dict()
    for key, value in inputs.items():
        if value:
            if "__" in key:
                if key.startswith("__") or key.endswith("__"):
                    last_filter_inputs[key.replace('__', "")] = value  # use for non nested fields like count or
                    # average
                else:
                    last_filter_inputs[key.replace('__', ".")] = value

            else:
                first_filter_inputs[key] = value

    first_filter = prepare_filter(
        inputs=first_filter_inputs,
        fields_names_for_regex=fields_names_for_regex,
        fields_names_for_range=fields_names_for_range,
        fields_names_for_in=fields_names_for_in,
        search_field_name=search_field_name,
        fields_names_for_search=fields_names_for_search,
    )

    last_filter = prepare_filter(
        inputs=last_filter_inputs,
        fields_names_for_regex=fields_names_for_regex,
        fields_names_for_range=fields_names_for_range,
        fields_names_for_in=fields_names_for_in,
        search_field_name=search_field_name,
        fields_names_for_search=fields_names_for_search,
    )

    return first_filter, last_filter
