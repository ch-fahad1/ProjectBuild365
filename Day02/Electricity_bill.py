units = float(input("Enter electricity units: "))

if units <= 100:
    bill = units * 10

elif units <= 200:
    bill = units * 15

elif units <= 300:
    bill = units * 20

else:
    bill = units * 25

print("Electricity Bill =", bill)