# Tip calculator
# day2 Project
print("I will do the tip math for you")
bill = float(input("What is the total bill? $"))
tip = int(input("How much are you tipping?10, 12, 15, or 20?"))
people = int(input("How many people are splitting the bill?"))
tipAsPercentage = tip / 100
totalTipAmount = bill * tipAsPercentage
totalBill = bill + totalTipAmount
billPerPerson = totalBill / people
finalAmount = round(billPerPerson, 2)
print(f"Each person will pay: ${finalAmount}  ")
