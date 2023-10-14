import logging
from functools import wraps

logging.basicConfig(
    filename='log.log',
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"calling function {func.__name__} with args {args}")
        res = func(*args, **kwargs)
        logging.info(f"function {func.__name__} return {res}")
    return wrapper

@log_decorator
def multiply(nb1: int, nb2: int):
    return nb1 * nb2



multiply(2, 2)


#https://www.tutorialspoint.com/How-to-get-a-function-name-as-a-string-in-Python#:~:text=The%20first%20approach%20is%20by,when%20the%20property%20is%20called.