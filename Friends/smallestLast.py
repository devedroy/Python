def leastLast(arr):
    least = arr[0]
    for n in arr:
        least = min(n,least)

    i = 0
    count = 0
    while i < len(arr):
        if arr[i] == least:
            arr.pop(i)
            count += 1
        i += 1
    
    arr.extend([least]*count)
        
    return arr

givenList = [5,12,5,8,10]
#res = [12,8,10,5,5]

print(leastLast(arr=givenList))