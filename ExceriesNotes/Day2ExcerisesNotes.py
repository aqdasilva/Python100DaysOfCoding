# day2 exercises and notes
# placement of character in a string
# print("Anthony"[0])  # subScripting first charater
# print("Anthony"[4])  # 5th character
#
# num_char = len(input("What is your name?"))
# new_numChar = str(num_char) #converts into a string
#
# print("Your name has " + new_numChar + " characters")
# print(type(num_char))

# # 2.1 exercises
# twoDigitNum = input("Select a two digit number: ")
# print(type(twoDigitNum))
# firstDigit = twoDigitNum[0]
# secondDigit = twoDigitNum[1]
# # #currently a string need to convert into int
# # result = int(firstDigit) + int(secondDigit) #int() converts into a int
#
# # # 2.2 BMI calculator
# # height = input("enter height in m: ")
# # weight = input("enter weight in kg: ")
# #
# # bmiCalc = int(weight) / float(height)**2 # **2 is to the second power
# # bms_as_int = int(bmiCalc) #converts into whole number
# # print(bms_as_int)
#
# #rounds into a whole number
# print(round(8 / 3))
#
# #rounds to the second place
# print(round(8 / 3, 2))
#
# #will divide 4/2 then 2/2
# result = 4 / 2
# result /= 2
# print(result)
#
# #user scores a point
# score = 0
# minusScore = 2
# score += 1
# minusScore -= 0
# isWinning = True
# #f-string
# print(f"Your score is {score}, you lost{minusScore}, you are winning{isWinning}")

# # life in weeks
# age = input("What is your current age?")
# ageAsInt = int(age) #converts age from str into int
# yearsRemaining = 100 - ageAsInt
# daysRemaining = yearsRemaining * 365
# weeksRemaining = yearsRemaining * 52
# monthsRemaining = yearsRemaining * 12
#
# finalMessage = f"You have{daysRemaining}, {weeksRemaining} weeks, {monthsRemaining} months"
# print(finalMessage)
