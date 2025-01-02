import difflib

string1 = input("Enter First String: ")
string2 = input("Enter Second String: ")

similarity = difflib.SequenceMatcher(None, string1, string2).ratio()

print(f"Similarity Ratio: {similarity:.2f}")