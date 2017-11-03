import turtle
bob = turtle.Turtle()
from myFunctionfile import*
turtle.colormode(255)
bob.speed(11)
turtle.bgcolor('black')

for c in ['red','white','blue','red','white','blue',]:

    stars(bob,c)
    bob.right(90)

turtle.done()
