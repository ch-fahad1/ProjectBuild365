year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is Not a Leap Year.")