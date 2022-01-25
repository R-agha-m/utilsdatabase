from os import environ
from utils_common.global_stg_loader import global_stg_loader

GlobalStg = global_stg_loader(current_stg_address=__file__,
                              stg_class_name="LocalStg")


class LocalStg:
    _debug_mode = None
    _report = None

    @property
    def DEBUG_MODE(self):
        if self._debug_mode is None:
            from utils_common.detect_boolean import detect_boolean
            self._debug_mode = detect_boolean(
                environ.get("DEBUG_MODE",
                            True))
        return self._debug_mode

    @property
    def report(self):
        if self._debug_mode is None:
            from utils_logging.get_or_create_logger import get_or_create_logger
            self._report = get_or_create_logger(
                destinations=("console",),
                level=10 if self.DEBUG_MODE else 20
            )
        return self._report


class StgClass(GlobalStg, LocalStg):
    pass


STG = StgClass()
report = STG.report

if __name__ == "__main__":
    print(STG.DEBUG_MODE)
    print(STG.report)
