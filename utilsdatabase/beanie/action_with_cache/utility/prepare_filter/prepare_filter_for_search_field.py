from re import escape


def prepare_filter_for_search_field(
        search_field_name: str,
        fields_to_search_on: tuple[str, ...],
        inputs: dict,
        filter_: list,
):
    # {"$and": [{'title': {"$regex": /g/}}, {'title': {"$regex": /i/}}]}
    if inputs.get(search_field_name):

        split_value = list()
        for i in inputs[search_field_name]:
            split_value.extend(i.split())

        if split_value:
            search_filter = list()
            for i in split_value:
                subfilter = list()
                for field_name in fields_to_search_on:
                    subfilter.append({field_name: {'$regex': escape(i)}})

                if len(subfilter) == 1:
                    search_filter.append(subfilter[0])

                elif len(subfilter) > 1:
                    search_filter.append({'$or': subfilter})

            if search_filter:
                filter_.append({'$and': search_filter})

    return filter_
