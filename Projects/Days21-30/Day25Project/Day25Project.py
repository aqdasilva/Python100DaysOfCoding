# Day25
# name that state game
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
allStates = data.state.to_list()
guessedStates = []

while len(guessedStates) < 50:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 States Correct",
                                   prompt="What is another states name? ").title()
    print(answerState)
    if answerState == "Exit":
        missingStates = []
        for state in allStates:
            if state not in guessedStates:
                missingStates.append(state)
        newData = pandas.DataFrame(missingStates)
        newData.to_csv("states_to_learn.csv")
        break

    if answerState in allStates:
        guessedStates.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.state == answerState]
        t.goto(int(stateData.x), int(stateData.y))
        t.write(answerState)
screen.exitonclick()
