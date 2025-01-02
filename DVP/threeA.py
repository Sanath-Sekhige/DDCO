sentence = input("Enter A Sentence: ")

wordCount = len(sentence.split())
digitCount = sum(n.isdigit() for n in sentence)
upperCount = sum(c.isupper() for c in sentence)
lowerCount = sum(c.islower() for c in sentence)

print(f"Number Of Words: {wordCount}")
print(f"Number Of Digits: {digitCount}")
print(f"Number Of Uppercase Letters: {upperCount}")
print(f"Number of Lowercase Letters: {lowerCount}")
