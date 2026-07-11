sentence = input("Enter Sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique Words:", len(unique_words))