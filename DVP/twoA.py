def F(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return F(n - 1) + F(n - 2)

N = int(input("Enter Integer N (N > 0): "))
if N <= 0:
    print("Error: N must be greater than 0")
else: 
    print(f"F({N}) = {F(N)}")