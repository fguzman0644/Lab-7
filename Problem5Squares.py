#Fernando Guzman
#02/28/25

#Function creates image shown on Lab 7 instructions

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

size = 10 ##Initial size of square
for i in range(5):##repeat 5 times
    alex.penup()
    alex.goto(-size/2,-size/2)##move turtle to center of next square
    alex.pendown()
    drawSquare(alex, size)
    size +=20 ##Increase the size of the square
    
wn.exitonclick()
