class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []]
        repeat1 = set()
        repeat2 = set()
        for n in nums1:
            if n not in nums2 and n not in repeat1:
                res[0].append(n)
                repeat1.add(n)
        for n in nums2:
            if n not in nums1 and n not in repeat2:
                res[1].append(n)
                repeat2.add(n)
        return res