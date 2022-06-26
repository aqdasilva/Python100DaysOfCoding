from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.xMove = 3
        self.yMove = 3
        self.moveSpeed = 0.1

    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX, newY)

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1  # reverse the x direction
        self.moveSpeed *= 0.8

    def resetPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.bounceX()
