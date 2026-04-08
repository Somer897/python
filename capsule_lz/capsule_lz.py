import os
import datetime
from functools import wraps
import csv

tb = []


#from datetime import date сегодня = date. today() print(f"Год: {сегодня. year}, Месяц: {сегодня. month}")
def log(func, tb: list):
    @wraps(func)
    def wrapper():
        #добавление строки информации
        a = [os.getlogin(), func.__name__, datetime.datetime.now(), datetime.now().strftime("%H:%M:%S")]
        tb.append(a)

        return tb
    return wrapper
        


def func1():
    print(func1.__name__)

def func2():
    print(func2.__name__)

def func3():
    print(func3.__name__)

def func4():
    print(func4.__name__) 

func1 = log(func1, tb)
func2 = log(func2, tb)
func3 = log(func3, tb)
func4 = log(func4, tb)
func1()
func2()
func3()
func4()

with open('logs.csv', 'w') as file:
     table = csv.writer(file)
     for i in tb:
        table.writerow(i)