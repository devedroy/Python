prerequisites = [[1,0],[0,1]]
preMap = {i:[] for i in range(2)}
print(preMap)

for crs, pre in prerequisites:
    # print(crs,pre)
    preMap[crs].append(pre)
print(preMap)
for crs in [0,1]:
    for pre in preMap[crs]:
        print(pre)