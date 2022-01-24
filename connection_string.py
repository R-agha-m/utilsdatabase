def create_connection_string(type_,
                             name,
                             username=None,
                             password=None,
                             host=None,
                             port=None):

    # dialect+driver://username:password@host:port/database
    connection_string = f'://{username}:{password}@{host}:{port}/{name}'
    if type_ in ("postgresql", "postgres"):
        return "postgresql" + connection_string

    elif type_ in ('mysql',):
        return 'mysql' + connection_string

    elif type_ in ('oracle',):
        return "oracle" + connection_string

    elif type_ in ('microsoft sql server', 'mssql'):
        return "mssql" + connection_string

    elif type_ in ("sqlite", 'sqlite3'):
        # sqlite://<nohostname>/<path>
        return f'sqlite:///{name}.sqlite3'
