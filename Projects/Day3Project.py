# day3 Project
# treasure island
print("Welcome to Treasure Island, \nYour mission is to find the Treasure")
firstChoice = input("You are at a crossroads. Where do you want to go? Type Left or Right").lower()


if firstChoice.lower() == "left":
    secondChoice = input("Do you want to swim or wait? ").lower()
    if secondChoice == "wait":
        thirdChoice = input("You arrrived on a island, you enter a cave with 3 doors. Pick one: Red, Yellow, and Blue").lower()
        if thirdChoice == "red":
            print("You just got sliced in half by a flaming axe = Game Over")
        elif thirdChoice == "yellow":
            print("You entered a cave and discovered the lost city of Atlantis Full of Treasure !!!")
        elif thirdChoice == "blue":
            print("You fell into a endless depth of ocean = Game Over")
        else:
            print("You choose a door that does not exist, A dragon comes and burns you for eternity")
    else:
        print("You walk into a imaginary hole that brings you into Mordor = Game Over")

