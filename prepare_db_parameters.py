from utils_common.load_parameters import load_parameters

MAIN_DB_PARAMETERS = {"TYPE": "MAIN_DB_TYPE",
                      "NAME": "MAIN_DB_NAME",
                      "USERNAME": "MAIN_DB_USER",
                      "PASSWORD": "MAIN_DB_PASSWORD",
                      "HOST": "MAIN_DB_HOST",
                      "PORT": "MAIN_DB_PORT",
                      "ENCODING": "MAIN_DB_ENCODING",
                      "POOL_SIZE": "MAIN_DB_POOL_SIZE",
                      "MAX_OVERFLOW": "MAIN_DB_MAX_OVERFLOW",
                      "POOL_RECYCLE": "MAIN_DB_POOL_RECYCLE"}

TEST_DB_PARAMETERS = {"TYPE": "TEST_DB_TYPE",
                      "NAME": "TEST_DB_NAME",
                      "USERNAME": "TEST_DB_USER",
                      "PASSWORD": "TEST_DB_PASSWORD",
                      "HOST": "TEST_DB_HOST",
                      "PORT": "TEST_DB_PORT",
                      "ENCODING": "TEST_DB_ENCODING",
                      "POOL_SIZE": "TEST_DB_POOL_SIZE",
                      "MAX_OVERFLOW": "TEST_DB_MAX_OVERFLOW",
                      "POOL_RECYCLE": "TEST_DB_POOL_RECYCLE"}

LOG_DB_PARAMETERS = {"TYPE": "LOG_DB_TYPE",
                     "NAME": "LOG_DB_NAME",
                     "USERNAME": "LOG_DB_USER",
                     "PASSWORD": "LOG_DB_PASSWORD",
                     "HOST": "LOG_DB_HOST",
                     "PORT": "LOG_DB_PORT",
                     "ENCODING": "LOG_DB_ENCODING",
                     "POOL_SIZE": "LOG_DB_POOL_SIZE",
                     "MAX_OVERFLOW": "LOG_DB_MAX_OVERFLOW",
                     "POOL_RECYCLE": "LOG_DB_POOL_RECYCLE"}


def read_raw_parameters(db_parameters,
                        can_use_config_file,
                        config_file,
                        parent_name_in_config_file,
                        default):
    raw_parameters = dict()
    for key, value in db_parameters.items():
        raw_parameters[key] = load_parameters(
            name=value,
            can_use_config_file=can_use_config_file,
            config_file=config_file,
            parent_name_in_config_file=parent_name_in_config_file,
            default=default
        )

    return raw_parameters
#
# def
#
#     @property
#     def MAIN_DB(self):
#         if self._main_db is None:
#             from utils_db import create_connection_string
#             # from db.models import base
#             self._main_db = {
#                 "TYPE": environ.get("MAIN_DB_TYPE"),
#                 "DBNAME": environ.get("MAIN_DB_DBNAME"),
#                 "USER": environ.get("MAIN_DB_USER"),
#                 "PASSWORD": environ.get("MAIN_DB_PASSWORD"),
#                 "HOST": environ.get("MAIN_DB_HOST"),
#                 "PORT": environ.get("MAIN_DB_PORT"),
#                 "ENCODING": 'utf-8',
#                 "POOL_SIZE": 1,
#                 "MAX_OVERFLOW": 0,
#                 "POOL_RECYCLE": 3600,
#                 # "BASE": base
#             }
#
#             if self.IS_MATRIX:
#                 connection_string = create_connection_string(
#                     type_=self._main_db["MAIN_DB_TYPE"],
#                     name=self._main_db["MAIN_DB_DBNAME"],
#                     username=self._main_db["MAIN_DB_USER"],
#                     password=self._main_db["MAIN_DB_PASSWORD"],
#                     host=self._main_db["MAIN_DB_HOST"],
#                     port=self._main_db["MAIN_DB_PORT"]
#                 )
#             else:
#                 connection_string = create_connection_string(
#                     type_='sqlite',
#                     name=f'{self.IO_DIR}{sep}localhost-main'
#                 )
#
#             self._main_db['CONNECTION_STRING'] = connection_string
#         return self._main_db
#
#     _main_db = None
#
#     @property
#     def MAIN_DB(self):
#         if self._main_db is None:
#             from utils_db import create_connection_string
#             from db.models import base
#             if self.IS_MATRIX:
#                 connection_string = create_connection_string(
#                     type_=environ["MAIN_DB_TYPE"],
#                     name=environ["MAIN_DB_DBNAME"],
#                     username=environ["MAIN_DB_USER"],
#                     password=environ["MAIN_DB_PASSWORD"],
#                     host=environ["MAIN_DB_HOST"],
#                     port=environ["MAIN_DB_PORT"]
#                 )
#             else:
#                 connection_string = create_connection_string(
#                     type_='sqlite',
#                     name=f'{self.IO_DIR}{sep}localhost-main'
#                 )
#
#             self._main_db = {
#                 'CONNECTION_STRING': connection_string,
#                 "ENCODING": 'utf-8',
#                 "POOL_SIZE": 1,
#                 "MAX_OVERFLOW": 0,
#                 "POOL_RECYCLE": 3600,
#                 "BASE": base
#             }
#         return self._main_db
