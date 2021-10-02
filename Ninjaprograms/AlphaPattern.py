## Read input as specified in the question.
## Print output as specified in the question.
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i = 1
while i <= n:
    j = 1
    charP = chr(ord('A') + i - 1)
    while j <= i:
        print(charP,end="")
        j = j + 1
    print()
    i = i + 1
