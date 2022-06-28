PLACEHOLDER = "[name]"


with open("Projects/Days21-30/Day24Project/input/names/invited_names.txt") as nameFiles:
    names = nameFiles.readlines()

with open(" ./input/letters/starting_letter.txt") as letterFile:
    letterContents = letterFile.read()
    for name in names:
        strippedName = name.strip()
        newLetter = letterContents.replace(PLACEHOLDER, name)
        with open(f"./output/readytosend/letter_for_{strippedName}.txt", mode="w") as completedLetter:
            completedLetter.write(newLetter)