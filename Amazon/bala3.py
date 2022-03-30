'''
1
5 5
0001X
XX1XX
001X1
00000
00000
'''

T = int(input())
for t in range(T):
    inpList = []
    ninp, j = map(int, input().split())
    for i in range(ninp):
        inpList.append(input())

    res = 0

    for s in inpList:
        for idx in range(len(s)):
            if s[idx] == 'X':
               break
            elif s[idx] == '1':
                res += 1
    print(res)
        