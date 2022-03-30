class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in nums:
            if (n - 1) not in numSet:
                maxLen = 0
                while (n + maxLen) in numSet:
                    maxLen += 1
                res = max(maxLen, res)
        return res