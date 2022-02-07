class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lenLIS, res = 0, 0

        for i in range(len(nums), -1, -1):
            maxLen, maxCnt = 1, 1

            for j in range(i + 1, len(nums)):