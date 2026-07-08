text = input("Enter sentence: ")
words = text.split()
shortest = words[0]

for word in words:

    if len(word) < len(shortest):
        shortest = word

print("Shortest Word:", shortest)