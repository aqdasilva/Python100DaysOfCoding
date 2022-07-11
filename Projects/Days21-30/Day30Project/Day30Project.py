# Day30

#file not found
try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["sdfsdf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_msg:
    print(f"that key{error_msg} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise KeyError
