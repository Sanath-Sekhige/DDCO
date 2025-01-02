test1 = int(input("Enter marks for test1: "))
test2 = int(input("Enter marks for test2: "))
test3 = int(input("Enter marks for test3: "))

totalMarks = test1 + test2 + test3
lowestMark = min(test1, test2, test3)

bestTwoAvg = (totalMarks - lowestMark) / 2
print("The best of two test avg marks: ", bestTwoAvg)