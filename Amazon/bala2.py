inp = [x for x in input().split()]
res = []
for i in range(1, int(inp[0])+1):
    if inp[i] == 'W':
        res.append('W')
print(' '.join(res))