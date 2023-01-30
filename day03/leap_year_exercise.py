# Calculates if input is a leap year of not based on the following conditions:
# The year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is not a leap year;unless...
# The year is also evenly divisible by 400. Then it is a leap year.

year=int(input("Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap=True
        else:
            leap=False
    else: 
        leap=True
else:
    leap=False

if leap==True:
    print("This is a leap year")
else:
    print("This is not a leap year")