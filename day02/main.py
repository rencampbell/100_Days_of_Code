#This program calculates total tip to be paid by each individual based on user input
print("Welcome to the tip calculator")
bill=float(input("What was the total bill? "))
tip=float(input("What percentage tip would you like to give? "))
people=float(input("How many people will split the bill? "))
total=round((tip/100*bill)/people,2)
print(f"Each person should pay ${total}")