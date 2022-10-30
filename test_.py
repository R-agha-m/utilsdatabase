# from os import environ, pathsep
# from pathlib import Path
# from sys import path as sys_path
#
# # environ["STG_MODULE_ADDRESS"] = "/home/ragham/Desktop/programming/utils_db/global_stg.py"
#
#
# from crud.crud import Crud
# try:
#     from .connection_string import create_connection_string
# except ImportError:
#     from connection_string import create_connection_string
#
# from tests.models import base
#
#
# crud_obj = Crud(connection_string='sqlite:///test.sqlite3',
#                 base=base)
# crud_obj.initiate()
