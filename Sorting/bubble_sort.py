def bubble_sort(arr):
    n = len(arr)
    swap = False
    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if swap == False:
            break
    return arr

A = [64, 25, 12, 22, 11]

print(bubble_sort(A))