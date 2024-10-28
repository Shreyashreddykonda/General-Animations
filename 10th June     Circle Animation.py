import turtle
import time

s1 = turtle.Screen()
s1.setup(800, 800)
t1 = turtle.Turtle()
t1.speed(20)


def circle1(x1, y1):
    t1.penup()
    t1.goto(x1, y1)
    t1.pendown()
    t1.fillcolor("red")
    t1.begin_fill()
    t1.circle(10)
    t1.end_fill()

def circle2(x2, y2):
    t1.penup()
    t1.goto(x2, y2)
    t1.pendown()
    t1.fillcolor("blue")
    t1.begin_fill()
    t1.circle(15)
    t1.end_fill()

def circle3(x3, y3):
    t1.penup()
    t1.goto(x3, y3)
    t1.pendown()
    t1.fillcolor("orange")
    t1.begin_fill()
    t1.circle(6)
    t1.end_fill()

def circle4(x4, y4):
    t1.penup()
    t1.goto(x4, y4)
    t1.pendown()
    t1.fillcolor("yellow")
    t1.begin_fill()
    t1.circle(9)
    t1.end_fill()
    
x1 = 0
y1 = 0

x2 = 5
y2 = 20

x3 = -10
y3 = -7

x4 = 14
y4 = -3

while True:
    circle1(x1, y1)
    circle2(x2, y2)
    circle3(x3, y3)
    circle4(x4, y4)
    x1 = x1 + 10
    y1 = y1 + 10
    x2 = x2 - 15
    y2 = y2 + 21
    x3 = x3 - 10
    y3 = y3 - 7
    x4 = x4 + 12
    y4 = y4 - 3
    time.sleep(1)
    t1.clear()
