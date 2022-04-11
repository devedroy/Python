
def mergeSortedArrays(arr1, arr2):
    res = []
    n, m = 0, 0

    while n < len(arr1) and m < len(arr2):
        if arr1[n] < arr2[m]:
            res.append(arr1[n])
            n += 1
        else:
            res.append(arr2[m])
            m += 1

    while n < len(arr1):
        res.append(arr1[n])
        n += 1

    while m < len(arr2):
        res.append(arr2[m])
        m += 1

    return res
    
arr1 = [1, 2, 4, 8]
arr2 = [3, 5, 6, 10]
print(mergeSortedArrays(arr1, arr2))