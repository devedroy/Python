class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = {}
        for n in nums:
            if n in countMap:
                countMap[n] += 1
            else:
                countMap[n] = 1
        res = nums[0]
        for k in countMap.keys():
            if countMap[k] >= countMap[res]:
                res = k
        return res 