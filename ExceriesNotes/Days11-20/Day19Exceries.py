# day19
# turtle graphics, event listeners, state & multiple instances

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveForwards():
    tim.forward(10)


def moveBackwards():
    tim.backward(10)


def turnLeft():
    newHeading = tim.heading() + 10
    tim.setheading(newHeading)

def turnRight():
    newHeading = tim.heading() - 10
    tim.setheading(newHeading)

def clear():
    #hit c button
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(moveForwards, "w")
screen.onkey(moveBackwards, "s")
screen.onkey(turnLeft, "a")
screen.onkey(turnRight, "d")
# bind key stroke to event
screen.exitonclick()

#state exampples
# timmy.color = green
# tommy.color = purple