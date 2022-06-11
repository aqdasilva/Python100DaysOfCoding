# Day 9

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again.",
                          }
# retrieving items from a dictionary
# print(programming_dictionary["Bug"])

# #adding new items to dict
# # programming_dictionary["Anthony"] = "The act of world dominance"
# # print(programming_dictionary)
#
# #create empty dict
# emptyDictionary = {}
#
# #wipe an existing dict
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# #edit a item in a dict
# # programming_dictionary["Bug"] = "A moth in your computer"
# # print(programming_dictionary)
#
# #loop thru a dict
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# ex 9.1
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "acceptable"
#     else:
#         student_grades[student] = "failed"
#
# print(student_grades)

# nesting....
capitals = {
    "france": "paris",
    "germany": "berlin"
}

# nesting a list into a dict
# travelLog = {
#     "france": {"cities_visited": ["paris", "lillie", "dijon"], "total visits": 12},
#     "germany": {"cities_visited": ["berlin", "hamburg", "stuggart"], "total visits": 14}
# }

# nesting a dict in a list
# travelLog = [
#     {"country": "france", "cities_visited": ["paris", "lillie", "dijon"], "total visits": 12},
#     {"country": "germany", "cities_visited": ["berlin", "hamburg", "stuggart"], "total visits": 14}
# ]


# ex 9.2
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# def add_new_country(countryVisited, timesVisited, citiesVisited):
#     newCountry = {}
#     newCountry["country"] = countryVisited
#     newCountry["visits"] = timesVisited
#     newCountry["cities"] = citiesVisited
#     travel_log.append(newCountry)
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


