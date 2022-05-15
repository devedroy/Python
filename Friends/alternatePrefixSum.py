
def prefixSum(a):
    n = len(a)
    for i in range(1, n):
        a[i] += a[i - 1]
    return a
n = 5
arr = [3, 1, 5, 1, 4]

res = prefixSum(arr)

resSum = 0
for i, n in enumerate(arr):
    if i % 2 == 0:
        resSum += n
    else:
        resSum -= n
print(resSum)