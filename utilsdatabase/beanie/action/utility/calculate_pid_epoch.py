from time import time
from random import randrange


def calculate_pid_epoch() -> int:
    return int(f"{time():.0f}{randrange(100, 1000)}")
