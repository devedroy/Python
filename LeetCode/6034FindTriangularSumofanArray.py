class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        def sumArr(arr):
            if len(arr) <= 2:
                return arr
            temp = []
            for i in range(len(arr) - 1):
                temp.append((arr[i] + arr[i + 1]) % 10)
            return sumArr(temp)
        
        res = sumArr(nums)
        return (sum(res)) % 10