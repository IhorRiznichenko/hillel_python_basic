from datetime import datetime

def time_it(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        elapsed = end - start
        print(f'Время выполнения функции: {elapsed}')
        return result
    return wrapper


@time_it
def func(word):
    if word == 'Yes':
        return True
    else:
        return False


@time_it
def area(b, h):
    return 0.5 * b * h

func('Yes')
area(2, 5)



