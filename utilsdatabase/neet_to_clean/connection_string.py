def create_connection_string(**kwargs):
    type_ = kwargs.get("type_") or kwargs.get("type") or kwargs["TYPE"]
    name = kwargs.get("name") or kwargs["NAME"]
    username = kwargs.get("username") or kwargs["USERNAME"]
    password = kwargs.get("password") or kwargs["PASSWORD"]
    host = kwargs.get("host") or kwargs["HOST"]
    port = kwargs.get("port") or kwargs["PORT"]

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
        connection_string = f'sqlite:///{name}'
        if connection_string.lower().endswith(("sqlite", "sqlite3",)):
            return connection_string
        else:
            return connection_string + ".sqlite3"
