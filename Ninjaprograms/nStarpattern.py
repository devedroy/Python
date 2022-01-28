#https://www.geeksforgeeks.org/pattern-printing-question-asked-cgi-coding-round/

#!/bin/python3
n = int(input())
i = 1
while i <= n:
    j = 1
    p = n - i + 1
    while j <= p:
        print(p,end='*')
        j += 1
    print()
    i += 1
