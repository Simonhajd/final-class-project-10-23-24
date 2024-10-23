import turtle
import random
import os

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def drawlines(size):
  t.pencolor(random.random(), random.random(), random.random())
  t.fillcolor("")
  t.begin_fill()
  for i in range(4):
    t.forward(size)
    t.right(random.randint(0, 360))
  t.end_fill()
  t.penup()
  t.goto(random.randint(-turtle.window_width() // 2, turtle.window_width() // 2),
       random.randint(-turtle.window_height() // 2, turtle.window_height() // 2))
  t.pendown()

def drawshapes(size):
  t.pencolor("")
  t.fillcolor(random.random(), random.random(), random.random())
  t.begin_fill()
  for i in range(4):
    t.forward(size)
    t.right(random.randint(0, 360))
  t.end_fill()
  t.penup()
  t.goto(random.randint(-turtle.window_width() // 2, turtle.window_width() // 2),
       random.randint(-turtle.window_height() // 2, turtle.window_height() // 2))
  t.pendown()

while True:
  drawlines(random.randint(0, 360))
  drawshapes(random.randint(0, 360))