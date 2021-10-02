n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= i - 1:
        print(" ",end="")
        s += 1
    k = 1
    while k <= n - i + 1:
        print("*",end="")
        k += 1
    print()
    i += 1
