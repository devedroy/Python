def zeroesToEnd(arr):
    # Write your code here.
    n = len(arr)
    i = 0
    j = 0
    while i < n and j < n:
        if arr[i] == 0:
            i += 1
        else:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
            i += 1
    return arr

arr = [10, 8, 0, 0, 12, 0]
print(zeroesToEnd(arr))