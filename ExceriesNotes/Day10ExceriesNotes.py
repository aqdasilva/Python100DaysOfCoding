# Day 10: functions with outputs

# def formatName(fName, lName):
#     formatFName = fName.title()
#     formatLName = lName.title()
#     return (f"{formatFName} {formatLName}")
#
#
# formatedString = formatName("anthony", "DASILVA")  # title converts first letter to capital
# print(formatedString)

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 True
#             else:
#                 False
#         else:
#             True
#     else:
#         False
#
# def days_in_month(year, month):
#     # if month > 12 or month < 1:
#     #     return "invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month-1]
#
#
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# docStrings


#calc with functions
