# Day18

# turtle graphics, tuples and importing modules
# from turtle import Turtle, Screen
#
# timmyTheTurtle = Turtle()
# timmyTheTurtle.shape("turtle")
# timmyTheTurtle.color("red")
# timmyTheTurtle.forward(100)
# timmyTheTurtle.right(90)

# for _ in range(4):
#     timmyTheTurtle.forward(100)
#     timmyTheTurtle.left(90)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# draws shape in for loop with line being random color
# colors = ["medium aquamarine", "green", "red", "firebrick", "deep pink", "purple", "indigo", "orange red"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")


def drawSpiroGraph(sizeOfGap):
    for _ in range(int(360 / sizeOfGap)):
        tim.color(randomColor())
        tim.circle(100)
        tim.setheading(tim.heading() + sizeOfGap)


drawSpiroGraph(5)
screen = t.Screen()
screen.exitonclick()

# for _ in range(200):
#     tim.color(randomColor())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# def drawShape(numSides):
#     angle = 360 / numSides
#     for _ in range(numSides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shapeSideN in range(3, 11):
#     tim.color(random.choice(colors))
#     drawShape(shapeSideN)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# import heroes
# print(heroes.gen())


# screen = Screen()
# # screen stays until clicked outta , stays at the bottom
# screen.exitonclick()
