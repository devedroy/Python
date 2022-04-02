class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        s  = [int(i) for i in bin(start)[2:]]
        g  = [int(i) for i in bin(goal)[2:]]
        res = 0
        
        while len(s) > 0 and len(g) > 0:
            if s[-1] == g[-1]:
                g.pop()
                s.pop()
                continue
            res += 1
            g.pop()
            s.pop()
            
        while len(s) > 0:
            if s[-1] == 0:
                s.pop()
                continue
            res += 1
            s.pop()
            
        while len(g) > 0:
            if g[-1] == 0:
                g.pop()
                continue
            res += 1
            g.pop()
            
        return res