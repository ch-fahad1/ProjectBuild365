numbers = [1, 2, 3, 2, 4, 2, 5]

item = int(input("Enter number: "))

count = 0

for num in numbers:
    if num == item:
        count += 1

print("Frequency =", count)