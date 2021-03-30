F1 = 0

F2 = 1

from turtle import *

bob = Turtle()

color('red')

bob.pu()

bob.goto(0,0)

bob.pd()

begin_fill()

pensize(5)

turnamount = 1

for(storage)in range (20):
    print(F1+F2)
    storage = F2
    F2 = F1+F2
    F1 = storage
    left(turnamount+5)
    forward(storage)
    turnamount = turnamount+5
