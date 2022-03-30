
class Solution:
    def solve(self, A, B, N):
        ans = 0
        hashMap = {}
        for i, n in enumerate(A):
            if n in hashMap:
                if B[i] < hashMap[n]:
                    ans -= hashMap[n]
                    del hashMap[n]
                    hashMap[n] = B[i]
                    ans += B[i]
                else:
                    continue
            else:
                hashMap[n] = B[i]
                ans += B[i]
        return ans
