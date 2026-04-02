import datetime
import os

def func1():
    print(func1.__name__)

def func2():
    print(func2.__name__)

def func3():
    print(func3.__name__)

def func4():
    print(func4.__name__)



def logger(func):
    def wrapper(*args):
        print(f'{os.getlogin()}\n{datetime.datetime.now()}\n{func.__name__}')
        f = open('logs.txt', 'f', encoding='UTF-8')
        f += f'{os.getlogin()}\n{datetime.datetime.now()}\n{func.__name__}'
        res = func(*args)
        print(f'{os.getlogin()}\n{datetime.datetime.now()}\n{func.__name__}')
        return res
    return wrapper



@logger
def glue(*args):
    res = ''
    for i in args:
        res /=i
    return  res

glue('str', 'btr')