# day7

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

endOfGame = False
lives = 6
wordList = ["anthony", "quinn", "dasilva"]
chosenWord = random.choice(wordList)

# testing code
print(f"solution is {chosenWord}")


display = []
wordLen = len(chosenWord)
for _ in range(wordLen):  # loop from 0 to length of the word
    display += "_"
print(display)


while not endOfGame:
    guessLetter = input("Guess a letter: ").lower()

    for position in range(wordLen):
        letter = chosenWord[position]
        print(f"Current Position: {position}\n Current Letter: {letter}\n Guessed Letter: {guessLetter}")
        if letter == guessLetter:
            display[position] = letter
    print(display)

    if guessLetter not in chosenWord:
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You lose :/")

    print(f"{ ' '.join(display)}")
    if "_" not in display:
        endOfGame = True
        print("You guessed all of the letters correctly !")

    print(stages[lives])
