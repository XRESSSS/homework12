import functools
import datetime

def logger(file_name='airport-codes_csv.csv'):
    def wrapper1(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(file_name, mode='a', encoding='utf-8') as file:
                file.write(f'{datetime.datetime.now()};{func.__name__};{result}\n')
            return result
        return wrapper
    return wrapper1

@logger()
def foo(arg):
    return arg * 2
foo(6)
