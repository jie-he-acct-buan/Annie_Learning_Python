import turtle
import math
import time


rocky = turtle.Turtle()
time.sleep(10)


#------------------------------------------------------------
# while loop
# -----------------------------------------------------------
rocky.reset()
shape = 0
while shape < 4:
    rocky.forward(100)
    rocky.left(90)
    shape = shape + 1


# -----------------------------------------------------------
# for loop
# -----------------------------------------------------------
rocky.reset()
rocky.pensize(2)
rocky.showturtle()
for shape in range(4):
    rocky.forward(100)
    rocky.left(90)

rocky.penup()
rocky.goto(100, 50)
rocky.left(90)
rocky.pendown()
rocky.color('purple')
rocky.circle(50)
rocky.hideturtle()


# -----------------------------------------------------------
# captian america shield
# -----------------------------------------------------------
# step 1: outside red circle 
rocky.reset()
rocky.pensize(1)
rocky.speed(10)
rocky.showturtle()
rocky.fillcolor('red')
rocky.begin_fill()
rocky.circle(200)
rocky.end_fill()


# step 2: white circle 
rocky.penup()
rocky.goto(0, 40)
rocky.pendown()
rocky.showturtle()
rocky.fillcolor('white')
rocky.begin_fill()
rocky.circle(160)
rocky.end_fill()


# step 3 : inside red circle
rocky.penup()
rocky.goto(0, 80)
rocky.pendown()
rocky.showturtle()
rocky.fillcolor('red')
rocky.begin_fill()
rocky.circle(120)
rocky.end_fill()

# step 4: blue circle
rocky.penup()
rocky.goto(0, 120)
rocky.pendown()
rocky.showturtle()
rocky.fillcolor('blue')
rocky.begin_fill()
rocky.circle(80)
rocky.end_fill()
rocky.hideturtle()


# step 5: star
rocky.penup()
rocky.goto(0, 280)
rocky.pendown()
rocky.showturtle()

import math
angle = 36 
length = math.cos((angle / 2) /360 * (2 * math.pi)) * 80 \
        - math.sin((angle / 2) /360 * (2 * math.pi)) * 80 * math.tan(angle/360 * (2 * math.pi))
rocky.right(90 + angle / 2)

rocky.pendown()
rocky.fillcolor('white')
rocky.begin_fill()
for i in range(5):
    rocky.forward(length)
    rocky.right(72)
    rocky.forward(length)
    rocky.left(180 - 36)
rocky.end_fill()
rocky.hideturtle()


time.sleep(5)
rocky.reset()
rocky.hideturtle()


# -----------------------------------------------------------
# Drawing a house
# -----------------------------------------------------------
rocky.reset()
turtle.Screen().bgcolor('lightblue')


# step 1: building
rocky.shape('turtle')
rocky.pensize(3)
rocky.fillcolor('yellow')
rocky.begin_fill()
for shape in range(4):
    rocky.forward(200)
    rocky.left(90)
rocky.end_fill()


rocky.penup()
rocky.goto(-30, 200)
rocky.pendown()
rocky.fillcolor('red')
rocky.begin_fill()
for shape in range(3):
    rocky.forward(260)
    rocky.left(120)
rocky.end_fill()


rocky.penup()
rocky.goto(60, 120)
rocky.pendown()
color = ['blue', 'red', 'orange', 'green']
for window in range(4):
    rocky.fillcolor(color[window])
    rocky.begin_fill()
    for shape in range(4):
        rocky.forward(30)
        rocky.left(90)
    rocky.right(90)    
    rocky.end_fill()


rocky.penup()
rocky.goto(110, 0)
rocky.pendown()
rocky.fillcolor('limegreen')
rocky.begin_fill()
for shape in range(2):
    rocky.forward(60)
    rocky.left(90)
    rocky.forward(120)
    rocky.left(90)
rocky.end_fill()


# step 2: snowman
rocky.shape('turtle')
rocky.shapesize(0.5)
rocky.pensize(3)
rocky.showturtle()

# body
rocky.penup()
rocky.goto(400, 0)
rocky.pendown()
rocky.fillcolor('white')
rocky.begin_fill()
rocky.circle(40)
rocky.end_fill()

# head
rocky.penup()
rocky.goto(400, 80)
rocky.pendown()
rocky.fillcolor('white')
rocky.begin_fill()
rocky.circle(30)
rocky.end_fill()

# buttons
for button in [60, 40, 20]:
    rocky.penup()
    rocky.goto(400, button)
    rocky.fillcolor('black')
    rocky.begin_fill()
    rocky.circle(5)
    rocky.end_fill()

# eyes
for eyes in [390, 410]:
    rocky.goto(eyes, 110)
    rocky.fillcolor('black')
    rocky.begin_fill()
    rocky.circle(5)
    rocky.end_fill()

# nose
rocky.pensize(1)
rocky.fillcolor('orange')
rocky.begin_fill()
rocky.goto(395, 98)
rocky.pendown()
rocky.goto(395, 103)
rocky.goto(418, 101.5)
rocky.goto(395, 98)
rocky.end_fill()
rocky.hideturtle()

# hello
rocky.penup()
rocky.goto(440, 150)
rocky.pensize(10)
rocky.pendown()
rocky.write('Hello!', font=('Arial', 15, 'normal'))

# arms




# step 3: Xmas tree
rocky.pensize(3)
rocky.shape('turtle')

# root
rocky.penup()
rocky.goto(-200, 0)
rocky.pendown()
rocky.fillcolor('brown')
rocky.begin_fill()
rocky.goto(-240, 0)
rocky.goto(-220, 20)
rocky.goto(-200, 0)
rocky.end_fill()

# first layer
rocky.penup()
rocky.goto(-160, 20)
rocky.pendown()
rocky.fillcolor('green')
rocky.begin_fill()
rocky.goto(-280, 20)
rocky.goto(-220, 80)
rocky.goto(-160, 20)
rocky.end_fill()

# second layer
rocky.penup()
rocky.goto(-170, 60)
rocky.pendown()
rocky.fillcolor('green')
rocky.begin_fill()
rocky.goto(-270, 60)
rocky.goto(-220, 100)
rocky.goto(-170, 60)
rocky.end_fill()

# third layer
rocky.penup()
rocky.goto(-180, 90)
rocky.pendown()
rocky.fillcolor('green')
rocky.begin_fill()
rocky.goto(-260, 90)
rocky.goto(-220, 130)
rocky.goto(-180, 90)
rocky.end_fill()

# star
rocky.penup()
rocky.goto(-220, 150)

angle = 36 
length = math.cos((angle / 2) /360 * (2 * math.pi)) * 15 \
        - math.sin((angle / 2) /360 * (2 * math.pi)) * 15 * math.tan(angle/360 * (2 * math.pi))
rocky.right(90 + angle / 2)

rocky.pendown()
rocky.fillcolor('gold')
rocky.begin_fill()
for i in range(5):
    rocky.forward(length)
    rocky.right(72)
    rocky.forward(length)
    rocky.left(180 - 36)
rocky.end_fill()
rocky.hideturtle()


time.sleep(5)


# step 4: snowflake






# -----------------------------------------------------------
# More loops practice
# -----------------------------------------------------------
# Q1:squares in diffrent colors 
rocky.reset()
rocky.pensize(3)
turtle.Screen().bgcolor('black')
rocky.color('white')


positions = [0, 60, 120, 180, 240, 300]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range (6):
    rocky.penup()
    # rocky.goto(positions[i], positions[i])
    rocky.goto(i * 60, 0)
    rocky.fillcolor(colors[i])
    rocky.pendown()
    rocky.begin_fill()
    for shape in range(4):
        rocky.forward(50)
        rocky.left(90)
    rocky.end_fill()    
rocky.hideturtle()
time.sleep(5)


# Q2:overlapping circles
rocky.reset()
rocky.pensize(3)
rocky.speed(0)
turtle.Screen().bgcolor('white')
rocky.color('black')

for i in range(36):
    rocky.circle(100)
    rocky.left(10)
rocky.hideturtle()
time.sleep(5)


# Q3:circle of circle
rocky.reset()
rocky.pensize(3)
rocky.speed(0)
turtle.Screen().bgcolor('black')
rocky.color('white')

for x in range(36):
    rocky.penup()
    rocky.forward(100)
    for i in range(6):
        rocky.penup()
        rocky.forward(20)
        rocky.pendown()
        rocky.circle(5) 
    rocky.penup()
    rocky.goto(0, 0)
    rocky.left(10)
rocky.hideturtle()
time.sleep(5)


# # Q4: Walmart
# rocky.reset()
# rocky.pensize(3)
# rocky.speed(0)
# turtle.Screen().bgcolor('white')
# rocky.color('orange')

# rocky.right(33.5)
# for x in range(6):
#     rocky.left(60)
#     rocky.penup()
#     rocky.forward(50)
#     for i in range(50):
#         rocky.forward(2)
#         rocky.pendown()
#         rocky.fillcolor('orange')
#         rocky.begin_fill()
#         rocky.circle(5 + 0.1* i) 
#         rocky.end_fill()
#         rocky.penup()
#     rocky.penup()
#     rocky.goto(0, 0)

# rocky.goto(-800, -60)
# rocky.color('dodger blue')
# rocky.pensize(100)
# rocky.write('Walmart', font=('Arial', 100))
# rocky.hideturtle()


# # Q5: rainbow
# rocky.reset()
# rocky.pensize(3)
# rocky.speed(0)
# turtle.Screen().bgcolor('lightblue')
# rocky.color('black')

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'lightblue']
# rocky.left(90)

# for i in range(8):
#     rocky.penup()
#     rocky.goto(300 - i * 20, 0)
#     rocky.fillcolor(colors[i])
#     rocky.begin_fill()
#     rocky.circle(300 - i * 20, 180)
#     rocky.end_fill()
#     rocky.left(180)

# rocky.hideturtle()






































