def prepare_skip_limit_for_aggregation(
        current_page: int = 1,
        page_size: int = 10,
) -> list[dict]:
    skip_limit_list = list()
    if page_size > 0:
        number_of_document_to_skip = max(current_page - 1, 0) * page_size
        skip_limit_list = [
            {'$skip': number_of_document_to_skip},
            {'$limit': page_size},
        ]

    return skip_limit_list
