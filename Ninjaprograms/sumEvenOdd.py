Even = 0
Odd = 0
N = int(input())
while N > 0:
    temp = N % 10
    if (temp % 2 == 0):
        Even += temp
    else:
        Odd += temp
    N = N // 10
print(Even," ",Odd)
