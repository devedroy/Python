class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        length = len(nums)
        nPairs = length // 2
        
        def countFreq(nums):
            n = len(nums)
            map = {}
            for i in range(n):
                if nums[i] in map.keys():
                    map[nums[i]] += 1
                else:
                    map[nums[i]] = 1
            return map
        
        mapper = countFreq(nums)
        
        if len(mapper) <= nPairs:
            for ele in mapper.values():
                if ele % 2 == 0:
                    res = True
                else:
                    return False
        else:
            res = False
        return res