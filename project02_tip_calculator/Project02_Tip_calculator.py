# Project 02: Tip Calculator - Spliting the bill

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $ "))
tip = float(input("What the percentage tip would you like to give: 10, 12 or 15? "))
tip_pct = (tip/100)+1
people = int(input("How many people to split the bill? "))
result = (bill*tip_pct)/people

print(f"Each person should pay: $ {result:.2f}")
