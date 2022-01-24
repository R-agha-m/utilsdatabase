from importlib import import_module
from os import environ
from utils_logging.get_or_create_logger import get_or_create_logger
from utils_common.detect_boolean import detect_boolean


class LocalStg:
    @property
    def DEBUG_MODE(self):
        return detect_boolean(
            environ.get("DEBUG_MODE",
                        True))

    @property
    def report(self):
        print("global")
        return get_or_create_logger(
            destinations=("console",),
            level=10 if self.DEBUG_MODE else 20
        )

