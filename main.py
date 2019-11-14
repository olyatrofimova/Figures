import turtle 
from turtle import *
def triangle(x, y, size, colour, angle):
    # TODO: (Olya)
    turtle.color(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.left(angle)
    turtle.foward(a)
    turtle.left(90)
    turtle.foward(a)
    turtle.goto(x, y)
    turtle.end_fill()
    turtle.penup()
    pass
def square(x, y, size, color, angle):
    # TODO: (Arina)
    turtle.goto(x, y)
    turtle.left(angle)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.penup()
    pass
def main():
    # TODO: (Olya) figure 1
    pass
    # TODO: (Olya) figure 2
    pass
    # TODO: (Arina) figure 3
    pass
    # TODO: (Arina) figure 4
    pass
    
