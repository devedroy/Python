class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        r = len(people) - 1
        l = 0
        res = 0
        
        flag = True             
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and people[l] <= remain:
                l += 1       
        return res