import datetime
import multiprocessing
import threading
import time

def a():
    lis = []
    for i in range(20000):
        lis.append(20000**(i))

if __name__ == '__main__':
    t = datetime.datetime.now()
    list1 = []
    for i in range(5):
        c = multiprocessing.Process(target=a)
        list1.append(c)
        c.start()
    
    for j in list1:
        j.join()

    print(datetime.datetime.now() - t)


if __name__ == '__main__':
    t = datetime.datetime.now()
    list1 = []
    for i in range(5):
        c = threading.Thread(target=a)
        list1.append(c)
        c.start()
    
    for j in list1:
        j.join()
        
    print(datetime.datetime.now() - t)
        
