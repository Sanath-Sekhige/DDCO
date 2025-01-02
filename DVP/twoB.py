def binaryToDecimal(binary):
    return int(binary, 2)

def octalToHex(octal):
    return hex(int(octal, 8))

binaryInput = input("Enter Binary Number: ")
decimal = binaryToDecimal(binaryInput)
print(f"Binary -> Decimal: {decimal}")

octalInput = input("Enter Octal Number: ")
hexa = octalToHex(octalInput)
print(f"Octal -> Hex: {hexa}")