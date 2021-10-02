n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n - i:
        print(" ",end="")
        s += 1
    j = 1
    k = i
    while j <= i:
        print(k,end="")
        j += 1
        k += 1

    k -= 2
    d = 1
    while d >= i:
        print(k,end="")
        k -= 1
        d += 1
    print()
    i += 1
