from sqlalchemy.exc import PendingRollbackError


def db_manipulation_by_dict(data,
                            crud):
    """ example of data
    data = (
                {'table': Request,
                 'filter': (or_(Request.request == request,
                                Request.id_2_crawl == id_2_crawl),),
                 "action": 'delete'},

                {'table': Channel,
                 'filter': (Channel.youtube_id == id_2_crawl,),
                 "action": 'delete'},

                {'table': RequestChild,
                 'filter': (or_(RequestChild.request == request,
                                RequestChild.child_id == id_2_crawl),),
                 "action": 'delete'},

                {'table': Request,
                 'key_values': {"request": request,
                                "id_2_crawl": id_2_crawl,
                                "task": task},
                 "action": 'create'},
             )"""
    added_data_2_db = list()
    for data_i in data:
        obj = None

        try:
            obj = core(data_i,
                       crud)

        except PendingRollbackError:
            crud.session.rollback()
            obj = core(data_i,
                       crud)

        if obj:
            added_data_2_db.append(obj)

    return added_data_2_db


def core(data_i,
         crud):
    if data_i['action'] == 'delete':
        getattr(crud.session.query(data_i['table']) \
                .filter(*data_i['filter']), "delete")()

    elif data_i['action'] in ('create', 'insert',):
        obj = data_i['table'](**data_i['key_values'])
        crud.insert(obj)
        return obj

    else:
        raise ValueError("Wrong action!")
