# PyPassword Generator
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+']

print("Welcome i will Generate a new password for you")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like? \n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))

# password = ""

# easy level
# say user picks 4
# for char in range(1, nr_letters + 1): # generates #1-4
#     password += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

#hard level
passwordList = []

for char in range(1, nr_letters + 1):
    passwordList.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    passwordList += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    passwordList += random.choice(numbers)

print(passwordList)
random.shuffle(passwordList)
print(passwordList)

password = ""
for char in passwordList:
    password += char

print(f"your password is: {password}")




