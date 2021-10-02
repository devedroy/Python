n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if j == 1:
            if i == 1:
                print(i,end="")
            else:
                print(i - 1,end="")
        else:
            if i == j:
                print(i - 1,end="")
            else:
                print(0,end="")
        j += 1
    print()
    i += 1
