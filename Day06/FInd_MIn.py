numbers = [10, 45, 23, 89, 12]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum =", minimum)