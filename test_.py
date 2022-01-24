from os import environ

# environ["STG_MODULE_ADDRESS"] = "/home/ragham/Desktop/programming/utils_db/global_stg.py"



from crud.crud import Crud
from utils_common.connection_string import create_connection_string
from tests.models import base


crud_obj = Crud(connection_string='sqlite:///test.sqlite3',
                base=base)
crud_obj.initiate()
