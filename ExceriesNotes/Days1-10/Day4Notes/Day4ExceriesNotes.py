# Day4
import random
import my_module  # imported this .py

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.pi)  # used the imported My_module here
#
# randomFloat = random.random() * 5
# print(randomFloat)
#
# loveScore = random.randint(1, 100)
# print(f"your love score is {loveScore}")

# #coin toss very simple
# randomSide = random.randint(0, 1)
# if randomSide == 1:
#     print("Heads")
# else:
#     print("Tails")
#
#
# statesOfAmerica = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
#                    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
#                    "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
#                    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
#                    "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
#                    "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
#                    "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
#                    "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
# print(statesOfAmerica[0]) #0 is the first position in the list, -1 is the last item in the list.
# statesOfAmerica[1] = "Alask0" #changes alaska into alask0
# statesOfAmerica.append("WonderfulLand") # append adds item to the end of the list
# statesOfAmerica.extend(["godland", "Mordor", "azeroth"]) #adds a list to a list
# #print(statesOfAmerica)

# # 4.4 Splits
# nameString = input("Give me everybody's names, seperated by a comma. ")
# names = nameString.split(", ")
# print(names)
#
# numItems = len(names)
# randomChoice = random.randint(0, numItems - 1)
# personWhoPays = names[randomChoice]
# print(personWhoPays + " is going to pay for our food today. ")
#
# #shorter version
# personWhoPays = random.choice(names)
# print(personWhoPays + " is going buy my food today." )

# # 4.6
# row1 = [" ", " ", " "]
# row2 = [" ", " ", " "]
# row3 = [" ", " ", " *"]  # row3
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure ? ")
#
# horizonal = int(position[0])  # 2
# vertical = int(position[1])  # 3
#
# selectedRow = map[vertical-1]
# selectedRow[horizonal - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")
