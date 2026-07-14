numbers = [10, 20, 30, 40]

try:
    index = int(input("Enter Index: "))

    print(numbers[index])

except IndexError:
    print("Error: Invalid index.")