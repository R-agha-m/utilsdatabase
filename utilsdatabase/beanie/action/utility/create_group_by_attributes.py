from .create_group_by_pipeline import DATETIME_BY_X_FORMAT


def create_group_by_attributes(
        attributes_names: tuple[str, ...]
) -> list[str]:
    group_by_attributes = list()
    for i in attributes_names:
        if i.endswith('_at'):
            for j in DATETIME_BY_X_FORMAT.keys():
                group_by_attributes.append(f'{i}{j}')

        else:
            group_by_attributes.append(i)

    return group_by_attributes