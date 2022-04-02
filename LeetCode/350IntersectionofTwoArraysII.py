class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        j = 0
        for n in nums1:
            if n in nums2:
                res.append(n)
                nums2.remove(n)
        return res

