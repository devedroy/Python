def countFreq(nums):
    n = len(nums)
    map = {}
    for i in range(n):
        if nums[i] in map.keys():
            map[nums[i]] += 1
        else:
            map[nums[i]] = 1
    return map

arr = [3,2,3,2,2,2]
mapper = countFreq(arr)
print(mapper)
print(len(mapper))
# for ele in mapper.values():
#     print(ele)
