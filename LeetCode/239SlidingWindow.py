#Monotonically decreasing queue
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
        
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     if not nums:
    #         return []
    #     if k == 1:
    #         return nums
    #     res = []
    #     queue = []
    #     for i in range(k):
    #         while queue and nums[i] >= nums[queue[-1]]:
    #             queue.pop()
    #         queue.append(i)
    #     res.append(nums[queue[0]])
    #     for i in range(k, len(nums)):
    #         if queue[0] == i - k:
    #             queue.pop(0)
    #         while queue and nums[i] >= nums[queue[-1]]:
    #             queue.pop()
    #         queue.append(i)
    #         res.append(nums[queue[0]])
    #     return res