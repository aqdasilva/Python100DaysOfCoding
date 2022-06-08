# day 8

# def greet():
#     print("ola")
#     print("how is your day going?")
#     print("have a great coding session")
# greet()
#
# def greetWithName(name):
#     print(f"Hello stranger {name}")
#     print(f"how is your day going ? {name}")
# greetWithName("Anthony")


# func with more than 1 input
# def greetWith(name, location):
#     print(f"hello {name}")
#     print(f"where is your fav place to visit? {location}")
#
#
# greetWith("Anthony", "Portugal")  # positional argument


# functions with keyword arguements, order doesnt matter because you declare it
# greetWith(name="Anthony", location="portugal")

# ex 8.1
import math

# def paintCalc(height, width, cover):
#     area = height * width
#     numOfCans = math.ceil(area / cover)
#     print(f"you will need {numOfCans} cans of paint")
#
#
# testH = int(input("height of the wall"))
# testW = int(input("width of the wall"))
# coverage = 5
#
# paintCalc(height=testH, width=testW, cover=coverage)

# def primeChecker(number):
#     isPrime = True
#     for i in range(2, number):
#         if number % i == 0:
#             isPrime = False
#         if isPrime:
#             print("its a prime number")
#         else:
#             print("its not a prime number")
#
#
# n = int(input("check this number: "))
# primeChecker(number=n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("type your messsage:\n").lower()
shift = int(input("type the shift number:\n"))


def encrypt(plainText, shiftAmount):
    cipherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"the encoded is {cipherText}")


encrypt(plainText=text, shiftAmount=shift)


def decrypt(ciperText, shiftAmount):
    plainText = ""
    for letter in ciperText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmount
        plainText += alphabet[newPosition]
    print(f"The decode text is {plainText}")


if direction == "encode":
    encrypt(plainText=text, shiftAmount=shift)
elif direction == "decode":
    decrypt(ciperText=text, shiftAmount=shift)


def caesar(starText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == "decode":
        shiftAmount *= -1
    for letter in starText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
        endText += alphabet[newPosition]
    print(f"the {cipherDirection} decoded text is {endText}")
