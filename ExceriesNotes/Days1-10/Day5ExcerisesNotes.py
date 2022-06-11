# Day5 Notes and Excerises

#
# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

# 5.1 EX
# takes a input and splits it into a list of heights
#
# studentHeights = input("Input a list of students heights ").split()
# for n in range(0, len(studentHeights)):
#     studentHeights[n] = int(studentHeights[n])
# print(studentHeights)
#
# totalHeight = 0
# for height in studentHeights:
#     totalHeight += height
# print(totalHeight)
#
# numberOfStudents = 0
# for student in studentHeights:
#     numberOfStudents += 1
#
# averageHeight = round(totalHeight / numberOfStudents)
# print(averageHeight)

# 5.2 Ex
# studentScores = input("Input a list of student scores")
# for n in range(0, len(studentScores)):
#     studentScores[n] = int(studentScores[n])
# print(studentScores)
#
# # print(max(studentScores)) #easiest way to find the highest value in the list
# # did to learn more for loops
# # loops through first 1 is higher than 0(highestscore) so highestscore turns into 1 until no more items exist in the list
# highestScore = 0
# for score in studentScores:
#     if score > highestScore:
#         highestScore = score
# print(f"The highest score: {highestScore}")

# adds every number from 1-100 to total = 5050
# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# 5.4 adding even numbers
#
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)
#
# total2 = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

# 5.4 fizzbuzz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)


