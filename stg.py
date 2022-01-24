from os import environ
from utils_logging.get_or_create_logger import get_or_create_logger
from utils_common.detect_boolean import detect_boolean

# todo: when a SETTING VARIABLE is not in global setting module and calculated in this module, it should be printed

# ========================================================================================================= debug mode
DEBUG_MODE = detect_boolean(
    environ.get("DEBUG_MODE",
                False))

# ============================================================================================================= logging
report = get_or_create_logger(
    destinations=("console",),
    level=10 if DEBUG_MODE else 20
)
