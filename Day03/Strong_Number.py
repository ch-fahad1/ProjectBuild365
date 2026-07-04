num = int(input("Enter a Number: "))

original = num
total = 0

while num > 0:

    digit = num % 10

    factorial = 1

    for i in range(1, digit + 1):
        factorial *= i

    total += factorial

    num = num // 10

if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")