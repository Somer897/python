from test_main import func
import math

def test_func():

    #test with all numbers
    a = func(1, 2, 3)
    """ a = -0.29000225377302247, its ok"""

    #if number in str
    b = func('1', 2, 3)
    """ b = -0.29000225377302247, just changed type of variable value"""

    #if we have str with letters
    c = func('str', 2, 3)
    """ c = None, Its all wrong? cause there are string type with letters"""

    #if cos = 0
    d = func(1, math.pi/2, 3)
    """ d = 1.3742264061666784e+16, its ok, cause there is no accurate value of PI"""

    #if radical is complex
    e = func(1, 2, -3)
    """ e = (-2.0220530613418997+1.7320508075688772j), its ok, cause there is a complex value"""
    print(a, b, c, d, e)

test_func()