from abc import abstractmethod, ABC
import math

class Figure(ABC):

    a: float


    @abstractmethod
    def S(self):
        ...

    @abstractmethod
    def P(self):
        ...


class Krug(Figure):
    def __init__(self, a):
        self.a = a

    def S(self):
        return(math.pi * self.a**2)

    def P(self):
        return(2 * math.pi * self.a)


class Treug(Figure):
    def __init__(self, a, angle, angle1, angle2, b, c):
        self.a =a
        self.angle = angle
        self.angle1 = angle1
        self.angle2 = angle2
        self.b = b
        self.c = c

    def S(self):
        p = (self.a + self.b + self.c) / 2
        return((p * (p - self.a) * (p - self.b) * (p - self.c))**0.5)

    def P(self):
        return(self.a + self.b + self.c)
    
class Trap(Figure):
    def __init__(self, a, angle, angle1, angle2, angle3, b, c, d):
        self.a = a
        self.angle = angle
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.b = b
        self.c = c
        self.d = d

    def S(self):
        h = math.tan(self.angle) * self.c
        return(h*(self.a+self.b)/2)
    
    def P(self):
        return(self.a + self.b + self.c + self.d)


class Pryamaugolnik(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def S(self):
        return(self.a * self.b)

    def P(self):
        return(self.a*2 + self.b*2)


circle = Krug(6)
treug = Treug(2, 1, 1, 1, 2, 2)
trap = Trap(2, 1.6, 1.6, 1.6, 1.6, 2, 2, 2)
pryam = Pryamaugolnik(2, 4)


def func1(a, b, c, d):
    print(a.S() + b.S() + c.S() + d.S())

def func2(a, b, c, d):
    print(a.P() + b.P() + c.P() + d.P())


func1(circle, circle, circle, circle)
func2(circle, circle, circle, circle)