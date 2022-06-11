from random import randint
from art import logo

easyLevel = 10
hardLevel = 5


def checkAnswer(guess, answer, turns):
    """checks answer against guess. returns the number of turns remaining"""
    if guess > answer:
        print("too high, like snoop dog")
        return turns - 1
    elif guess < answer:
        print("too low, like a stripper")
        return turns - 1
    else:
        print(f"you sniped it out ! the answer was {answer}")


def setDifficulty():
    level = input("choose a difficulty. type 'noob' or 'extreme': ")
    if level == "noob":
        return easyLevel
    else:
        return hardLevel


def game():
    print(logo)
    print("Welcome to Guess a Number Stoopid !")
    print("I am thinking of a special number between 1 and 100")

    attemptsLeft = 10
    answer = randint(1, 100)
    turns = setDifficulty()
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess a number, before jigsaw comes gets you")
        guess = int(input("make a guess, sucka: "))
        turns = checkAnswer(guess, answer, turns)
        if turns == 0:
            print("your put of guesses, and fall off a cliff")
            return
        elif guess != answer:
            print("guess again. *facepalm*")

    print(f"you have {turns} attempts left before something eats you in your sleep")


game()
