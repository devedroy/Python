class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}
        if len(s) != len(t):
            return False

        for c in s:
            if c not in smap.keys():
                smap[c] = 1
            smap[c] += 1
        print(smap)
        
        for c in t:
            if c not in tmap.keys():
                tmap[c] = 1
            tmap[c] += 1
        print(tmap)
    
        for c in smap.keys():
            if c not in tmap.keys():
                return False
            if smap[c] != tmap[c]:
                return False
        return True

s = Solution()
res = s.isAnagram("aacc", "ccac")
print(res)