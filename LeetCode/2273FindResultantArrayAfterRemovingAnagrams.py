class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(s, t):
            smap, tmap = {}, {}
            if len(s) != len(t):
                return False
            for c in s:
                if c not in smap.keys():
                    smap[c] = 1
                smap[c] += 1
            for c in t:
                if c not in tmap.keys():
                    tmap[c] = 1
                tmap[c] += 1
            for c in smap.keys():
                if c not in tmap.keys():
                    return False
                if smap[c] != tmap[c]:
                    return False
            return True
        
        length = len(words)
        i = 1
        while i < length:
            if isAnagram(words[i - 1], words[i]):
                words.remove(words[i])
                length = len(words)
                continue
            i += 1
        return words