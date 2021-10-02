n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n - i:
        print(" ",end="")
        s += 1
    j = 1
    while j <= i:
        print("*",end="")
        j += 1
    d = i - 1
    while d >= 1:
        print("*",end="")
        d -= 1
    print()
    i += 1
