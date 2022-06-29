# Day25
# working with CSV files & analysing data with pandas

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# # print(data)
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #get data in columns
# print(data["condition"])
# print(data.condition)
#
# # get data from row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # get condition for certain day
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
#
# # calculate c to f
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
# print(monday.condition)
#
# #create dataframe from scratch
# data_dict = {
#     "students": ["amy", "james", "angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
greySquirrel = len(data[data["Primary Fur Color"] == "Gray"])
redSquirrel = len(data[data["Primary Fur Color"] == "Red"])
blackSquirrel = len(data[data["Primary Fur Color"] == "Black"])
print(greySquirrel)
print(redSquirrel)
print(blackSquirrel)

data_dict = {
    "Fur Color": [ "Gray", "Cinnamon", "Black"],
    "Count": [greySquirrel, redSquirrel, blackSquirrel]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("nycSquirrelCount.csv")