class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        h = 1
        v = 1
        for i in range(1, len(nums) - 1):
            l = i - 1
            r = i + 1
            
            if nums[i] > nums[l] and nums[i] > nums[r]:
                h += 1
            if nums[i] < nums[l] and nums[i] < nums[r]:
                v += 1
            if nums[i] == nums[l]:
                l -= 1
                if nums[i] > nums[l] and nums[i] > nums[r]:
                    h += 1
                if nums[i] < nums[l] and nums[i] < nums[r]:
                    v += 1
            if nums[i] == nums[l]:
                r += 1
                if nums[i] > nums[l] and nums[i] > nums[r]:
                    h += 1
                if nums[i] < nums[l] and nums[i] < nums[r]:
                    v += 1
        return h