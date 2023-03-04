def subarraySum(nums,k):
    i, res = 0, 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            tempSum = sum(nums[i:j+1])
            if tempSum == k:
                res += 1
    return res
    
nums = [1,1,1]
k = 2
result = subarraySum(nums=nums, k=k)
print(result)