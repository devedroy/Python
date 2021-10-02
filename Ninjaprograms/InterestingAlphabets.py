n = int(input())
i = 1
while i <= n:
    j = 1
    p = n - i + 1
    while j <= i:
        charP = chr(ord('A') + p - 1)
        print(charP,end="")
        p = p + 1
        j = j + 1
    print()
    i = i + 1
