for i in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    acc = 0 #subarray length
    des = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            des += 1
        if arr[i] < arr[i + 1]:
            acc += 1
    print(max(acc, des) + 1)