arr = [2, 7, 5, 9, 0]
res = arr[0]
for ele in arr:
    if res < ele:
        res = ele
print(res)