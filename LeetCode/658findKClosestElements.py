from ast import List

from sympy import re


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        val, idx = arr[0], 0

        while l <= r:
            m = (l + r) // 2
            curDiff, resDiff = abs(arr[m] - x), abs(arr[idx] - x)
            if (curDiff < resDiff) or (curDiff == resDiff and arr[m] < arr[idx]):
                idx = m
                val = arr[m]
            
#https://github.com/neetcode-gh/leetcode/blob/main/658-Find-K-Closest-Elements.py

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2

            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l : l + k]