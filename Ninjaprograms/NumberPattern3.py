n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        if j == 1:
            print(1,end="")
        else:
            if i == j:
                print(1,end="")
            else:
                print(2,end="")
        j += 1
    print()
    i = i + 1
