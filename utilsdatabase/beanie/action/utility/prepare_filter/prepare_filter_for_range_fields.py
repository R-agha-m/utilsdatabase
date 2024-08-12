def prepare_filter_for_range_fields(
        fields_names: tuple[str, ...],
        inputs: dict,
        filter_: list,
):
    for field_name in fields_names:
        from_ = field_name + '_from'
        to = field_name + '_to'
        include_null = field_name + '_include_null'

        sub_filter = dict()
        or_filter = list()
        if inputs.get(from_) is not None:
            sub_filter['$gte'] = inputs[from_]

        if inputs.get(to) is not None:
            sub_filter['$lt'] = inputs[to]

        if sub_filter:
            or_filter.append({field_name: sub_filter})

        if inputs.get(include_null):
            or_filter.append({field_name: None})

        if or_filter:
            filter_.append({'$or': or_filter})

    return filter_
