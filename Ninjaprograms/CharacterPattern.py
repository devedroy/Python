n = int(input())
i = 1
while i <= n:
    j = 1
    p = i
    while j <= i:
        charP = chr(ord('A') + p - 1)
        print(charP,end = "")
        j = j + 1
        p = p + 1
    print()
    i = i + 1
