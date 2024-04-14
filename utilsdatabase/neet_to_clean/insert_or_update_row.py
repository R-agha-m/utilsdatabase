

def insert_or_update_row(table,
                         filter_,
                         data_2_save,
                         crud):
    obj = crud.session.query(table) \
        .filter(*filter_).one_or_none()

    if obj is None:
        obj = table(**data_2_save)
        crud.insert(obj)
    else:
        for key, value in data_2_save.items():
            if getattr(obj, key) != value:
                setattr(obj, key, value)
        crud.session.commit()
