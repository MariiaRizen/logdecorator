import logging
from functools import wraps


logging.basicConfig(
    filename='log.txt',
    level=logging.DEBUG,
    # format='%(levelname)s %(name)s %(message)s'
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


print(test_function1(2, 5))
print(test_function2())
