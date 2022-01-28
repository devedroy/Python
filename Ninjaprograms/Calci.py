loop = True
while loop:
    n = int(input())
    while n > 6:
        print("Invalid Operation")
        n = int(input())
    if n == 6:
        loop = False
    else:
        a = int(input())
        b = int(input())

        if n == 1:
            print(a + b)
        elif n == 2:
            print(a - b)
        elif n == 3:
            print(a * b)
        elif n == 4:
            print(a // b)
        elif n == 5:
            print(a % b)