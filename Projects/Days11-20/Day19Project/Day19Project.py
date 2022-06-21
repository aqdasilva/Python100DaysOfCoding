import turtle
from turtle import Turtle, Screen
import random

isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="make your bet ", prompt="which turtle will win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []

print(userBet)

for turtleIndex in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.penup()
    newTurtle.color(colors[turtleIndex])
    newTurtle.goto(x=-230, y=yPositions[turtleIndex])
    allTurtles.append(newTurtle)

if userBet:
    isRaceOn = True

while isRaceOn:
    for turtle in allTurtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winningColor = turtle.pencolor()
            if winningColor == userBet:
                print(f"you won ! the {winningColor} turtle is the winner")
            else:
                print(f"you lost ! the {winningColor} turtle is the winner")
        randDistance = random.randint(0, 10)
        turtle.forward(randDistance)

screen.exitonclick()
