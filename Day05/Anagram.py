word1 = input("First Word: ")
word2 = input("Second Word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Anagram")
else:
    print("Not Anagram")