B = [10, 20, 30, 15, 17, 19, 7]
d = {1: [10, 20, 17], 3: [15, 19], 5: [30, 7]}
c = {}
for i in d.keys():
    avg = sum(d[i]) / len(d[i])
    for n in d[i]:
       c[n] = int(avg)
res = []
for i in B:
    res.append(i - c[i])
print(res)