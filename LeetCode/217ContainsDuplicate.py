class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lol = set()
        
        for _ in nums:
            if _ in lol:
                return True
            else:
                lol.add(_)
        return False