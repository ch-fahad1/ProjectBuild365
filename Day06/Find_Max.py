numbers = [10, 45, 23, 89, 12]

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum =", maximum)