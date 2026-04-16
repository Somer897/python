from abc import abstractmethod, ABC

class animal(ABC):

    @abstractmethod
    def eat():
        ...
    
    def move():
        ...

class Bear(animal):
    ...

a = Bear

def func1():
    a.move()