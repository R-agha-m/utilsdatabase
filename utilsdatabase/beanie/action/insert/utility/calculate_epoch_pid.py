from time import time
from random import randrange


def calculate_epoch_pid() -> int:
    return int(f"{time():.0f}{randrange(1000, 10000)}")
