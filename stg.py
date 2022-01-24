from os import environ
from utils_logging.get_or_create_logger import get_or_create_logger
from utils_common.detect_boolean import detect_boolean
from utils_common.global_stg_loader import global_stg_loader


GlobalStg = global_stg_loader()


class LocalStg:
    @property
    def DEBUG_MODE(self):
        return detect_boolean(
            environ.get("DEBUG_MODE",
                        True))

    @property
    def report(self):
        print("local")
        return get_or_create_logger(
            destinations=("console",),
            level=10 if self.DEBUG_MODE else 20
        )


class StgClass(GlobalStg, LocalStg):
    pass


STG = StgClass()
report = STG.report

if __name__ == "__main__":
    print(STG.DEBUG_MODE)
    print(STG.report)
