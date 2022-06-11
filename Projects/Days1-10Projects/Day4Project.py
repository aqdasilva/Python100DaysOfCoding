# Day4 Project
#rock, paper, scissors !
import random

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computerChoose = random.randint(0, 2)
print(f"Computer chose {computerChoose}")

if choose == 0 and computerChoose == 2:
    print("You wins !")
elif choose >= 3 or choose < 0:
    print("You typed a invalid number, you lose ! ")
elif computerChoose == 0 and choose == 2:
    print("You lose ")
elif choose > computerChoose:
    print("You win")
elif computerChoose > choose:
    print("You Lose")
elif choose == computerChoose:
    print("Its a draw !")

