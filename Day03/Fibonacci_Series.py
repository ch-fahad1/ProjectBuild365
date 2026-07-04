num = int(input("Enter how many Fibonacci numbers: "))

first = 0
second = 1

print(first)

print(second)

for i in range(num - 2):
    next = first + second
    print(next)

    first = second
    second = next