from urllib.parse import quote_plus


def create_connection_string_mongodb(config):
    host = getattr(config, 'HOST')
    port = getattr(config, 'PORT')
    database = getattr(config, 'DATABASE', None)
    username = getattr(config, 'USERNAME', None)
    password = getattr(config, 'PASSWORD', None)
    authdb = getattr(config, 'AUTHDB', None)

    connection_string = "mongodb://"

    if username:

        connection_string += f"{quote_plus(username)}:{quote_plus(password)}@"

    connection_string += f"{host}:{port}/"

    if database:
        connection_string += f"{database}"

    if authdb:
        connection_string += f"?authSource={authdb}"

    return connection_string, database
