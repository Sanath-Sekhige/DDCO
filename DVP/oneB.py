num = input("Enter a number: ")

if num == num[::-1]:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")

digitCount = {}
for digit in num:
    digitCount[digit] = digitCount.get(digit, 0) + 1

print("Occurances of each digit")
for digit, count in digitCount.items():
    print(f"Digit: {digit}, Count: {count}")