import turtle
import math

s1 = turtle.Screen()
s1.setup(800, 800)
s1.bgcolor("light green")

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.color("blue")
t2.color("yellow")
t3.color("red")
t1.shape('circle')
t3.shape('circle')

t1.goto(0, 0)
t2.goto(0, 0)
t2.begin_fill()
t2.circle(30)
t2.end_fill()
t1.pendown()

theta = 0
theta1 = 0
delta = 0
delta1 = 0
a = 150
r = 200
t1.penup()

while True:
    for theta in range(0, 360, 1):
        delta = theta1
        theta1 = math.radians(theta)
        delta1 = theta1
        x1 = a*math.cos(theta1)
        y1 = a*math.sin(theta1)
        x2 = r*math.cos(delta1)
        y2 = r*math.sin(delta1)
        t1.goto(x1, y1)
        t3.goto(x2, y2)
