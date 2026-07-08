numbers = [11, 24, 35, 48, 50]

largest = None

for num in numbers:

    if num % 2 == 0:

        if largest is None or num > largest:
            largest = num

print("Largest Even =", largest)