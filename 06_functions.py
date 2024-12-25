import time
import math
import turtle
import random


shape = turtle.Turtle()
shape.reset()

#  draw a square
def square(length):
    for i in range(4):
        shape.forward(length)
        shape.left(90)


# draw a triangle
def triangle(length):
    for i in range(3):
        shape.forward(length)
        shape.left(120)

shape.reset()
for i in range(100):
    square(100)
    shape.left(3.6)



shape.reset()
square_color = ['red', 'orange', 'green', 'blue']
# triangle_color
for i in range(4):
    shape.fillcolor(square_color[i])
    shape.begin_fill()
    for j in range(4):
        shape.forward(200)
        shape.left(90)
    shape.end_fill()        
    shape.right(90)




def window(length=100, square_color=['red', 'orange', 'green', 'blue']):
    for i in range(4):
        shape.fillcolor(square_color[i])
        shape.begin_fill()
        for j in range(4):
            shape.forward(length)
            shape.left(90)
        shape.end_fill()        
        shape.right(90)    




# 7 by 7 rainbow squares
def rainbow_squares(length=20, gap=10):
    shape.speed(0)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
    for k in range(7):
        shape.penup()
        shape.goto(0, k * (length + gap))
        shape.pendown()
        for i in range(7):
            shape.fillcolor(colors[i])
            shape.begin_fill()
            for _ in range(4):
                shape.forward(length)
                shape.left(90)
            shape.end_fill()
            shape.penup()
            shape.forward(length + gap)    
            shape.pendown()


shape.reset() 
shape.speed(0)
rainbow_squares(-20, 10)



# calculate your average score
scores = [10, 20, 30, 44, 33]

def average(scores):
    summ = 0
    for i in range(len(scores)):
        summ = summ + scores[i]
    
    average = summ / len(scores)
    return average


# sum of a series

def summ(n):
    summ = 0
    for i in range(1, n + 1):
        summ = summ + i
    return summ
summ(10)
    
# factorial of a number

def factorial(n):   
    factor = 1
    for i in range(1, n + 1):
        factor = factor * i
    return factor     
factorial(10)




summ = 0
for i in range(1, 11, 1):
    summ = summ + i
print(summ)


summ = 0
i = 1
while i <= 10:
    summ = summ +  i
    i = i + 1
print(summ)



for i in range(0, 11, 1):
    print(i / 10)

i = 0
while i <= 1:
    print(i)
    i = round(i + 0.1, 1)

