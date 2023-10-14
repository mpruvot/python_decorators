import logging
from functools import wraps

logging.basicConfig(
    filename='log.log',
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

class Player:
    def __init__(self, name: str, pv: int, lvl: int) -> None:
        self.name = name
        self.pv = pv
        self.lvl = lvl

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"calling function {func.__name__} with args {args} and kwargs {kwargs}")
        res = func(*args, **kwargs)
        logging.info(f"function {func.__name__} return {res}")
    return wrapper

@log_decorator
def new_player(pv: int, lvl: int, name: str):
    print(f"Player {name} is lvl {lvl} and has {pv} lp !")
    return Player(name, pv, lvl)


new_player(100, 20, name="Marius")


#https://www.tutorialspoint.com/How-to-get-a-function-name-as-a-string-in-Python#:~:text=The%20first%20approach%20is%20by,when%20the%20property%20is%20called.
#https://www.youtube.com/watch?v=4jBJhCaNrWU