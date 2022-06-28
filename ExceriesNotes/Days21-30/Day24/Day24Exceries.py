# day 24
# working with local files and directories

with open("my_file.txt") as file:
    file = open("my_file.txt")
contents = file.read()  # takes the contents in file as a STRING
print(contents)
file.close()  # need to close file because it takes up resources on your computer

with open("new_file.txt", mode="w") as file:
    file.write("\nNew Text.")
