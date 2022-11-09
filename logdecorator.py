import logging
import math
from functools import wraps
from math import factorial


logging.basicConfig(
    filename='log.txt',
    level=logging.DEBUG,
    format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
)


def log_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        resp = f(*args, **kwargs)
        logging.info(f'Name function is {f.__name__}. result is {resp}. Parametrs are {args}, {kwargs}')
        return resp
    return wrapper


@log_decorator
def test_function1(a, b):
    return sum((a, b))


@log_decorator
def test_function2():
    print('hello')


@log_decorator
def test_function3(c):
    return math.factorial(c)


if __name__ == "__main__":

    print(test_function1(2, 5))
    print(test_function2())
    print(test_function3(4))

