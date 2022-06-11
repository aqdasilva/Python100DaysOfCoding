# Day3
# print("Welcome to DisneyLand !")
# height = int(input("What is your height in Inches? "))
#
# # = assigning to variable
# ## == check equality
#
# if height > 45:
#     print("You are tall enough !")
# else:
#     print("You need to grow a lil more :( ")
#
# # exercise 3.1
# number = int(input("Which number do you want to check? "))
# mod = number % 2
# if mod > 0:
#     print("This is an odd number")
# # else:
# # #     print("This is a even number")
# #
# print("Welcome to DisneyLand !")
# height = int(input("What is your height in Inches? "))
# bill = 0
#
# if height >= 45:
#     print("You are tall enough !")
#     age = int(input("What is your age? "))
#     if age < 12:  # inner if loop
#         bill = 25
#         print("Pay up $25")
#     elif age <= 18:
#         bill = 12
#         print("Pay up $12")
#     elif age >= 45 and age <= 55:
#         print("Everything is taking care of, Free ride on us !")
#     else:
#         bill = 15
#         print("Pay up $15")
#
#     wants_photo = input("Do you want a photo taken? Y or N ")
#     if wants_photo == "Y":
#         bill += 3  # current bill then adds $3
#     print(f"Your final bill is = {bill} ")
#
# else:
#     print("You need to grow a lil more :( ")

# #Exercise 3.2
#
# height = float(input("Enter your height in M: "))
# weight = float(input("Enter your weight in KG: "))
# bmiCalc = int(weight) / float(height)**2
# bmiAsInt = int(bmiCalc)
# print(bmiAsInt)
# if bmiAsInt <= 18.5:
#     print("You are underWeight ")
# elif bmiAsInt <= 25:
#     print("You are normal weight")
# elif bmiAsInt <= 30:
#     print("You are overweight")
# elif bmiAsInt <= 35:
#     print("You are Obese")
# else:
#     print("You are clinically obese")

# # 3.3 Excerise
#
# def checkYear(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# year = int(input("Which year do you want to check ?"))
# if (checkYear(year)):
#     print("This is a leap year")
# else:
#     print("Not a leap year")

# # 3.4
# print("Wlecome to Python Pizza Deliveries !")
# size = input("What size pizza do you want to devour ? S, M , L, or XL")
# addPepperoni = input("Do you want pepperoni? Y or N")
# extraCheese = input("Do you want extra cheese? Y or N ")
# addPineapple = input("Do you want pineapple? Y or N ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# elif size == "XL":
#     bill += 35
# if addPepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extraCheese == "Y":
#     bill += 1
# if addPineapple == "Y":
#     if size == "S":
#         bill += 4
#     elif size == "M":
#         bill += 8
#     else:
#         bill += 12
#
# print(f"Your final bill is: {bill}")
#
# # 3.5 love calculator
# print("Welcome to the Love Calculator")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# combineNames = name1 + name2
# lowerCaseNames = combineNames.lower()  # changes all input into lowercase
# t = lowerCaseNames.count("t")
# r = lowerCaseNames.count("r")
# u = lowerCaseNames.count("u")
# e = lowerCaseNames.count("e")
#
# true = t + r + u + e
#
# l = lowerCaseNames.count("l")
# o = lowerCaseNames.count("o")
# v = lowerCaseNames.count("v")
# e = lowerCaseNames.count("e")
#
# love = l + o + v + e
#
# loveScore = int(str(true) + str(love))
#
# if (loveScore < 10) or (loveScore > 90):
#     print(f"Your love score is {loveScore}, you go together like coke and mentos")
# elif(loveScore >= 40) and (loveScore <= 50):
#     print(f"Your score is {loveScore}, you are alright together")
# else:
#     print(f"your score is {loveScore}")
