def create_connection_string_mongodb(config):
    host = getattr(config, 'host')
    port = getattr(config, 'port')
    database = getattr(config, 'database', None)
    username = getattr(config, 'username', None)
    password = getattr(config, 'password', None)
    authdb = getattr(config, 'authdb', None)

    connection_string = "mongodb://"

    if username:
        connection_string += f"{username}:{password}@"

    connection_string += f"{host}:{port}/"

    if database:
        connection_string += f"{database}"

    if authdb:
        connection_string += f"?authSource={authdb}"

    return connection_string, database
