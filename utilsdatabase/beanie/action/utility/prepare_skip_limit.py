def prepare_skip_limit(
        current_page: int = 1,
        page_size: int = 10,
) -> dict:
    skip_limit_dictionary = dict()
    if page_size > 0:
        number_of_document_2_skip = max(current_page - 1, 0) * page_size

        skip_limit_dictionary["skip"] = number_of_document_2_skip
        skip_limit_dictionary["limit"] = page_size

    return skip_limit_dictionary
