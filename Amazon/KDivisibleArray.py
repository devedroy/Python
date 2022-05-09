from ast import List


class Solution:
    def solve(self, N : int, K : int, A : List[int]) -> int:
        # code here
        s = 0
        c = 0
        # while (s!=K):
        #     for i in A:
        #         if i%K==0:
        #             s+=1
        #         elif (i + 1) % K == 0 or (i - 1) % K == 0:
        #             s+=1
        #             c+=1
        for i in A:
            if s<=K:
                
                if i%K==0:
                    s+=1
                elif (i + 1) % K == 0 or (i - 1) % K == 0:
                    s+=1
                    c+=1

        return c

N = 5
K = 4
A = [4, 7, 9, 5, 2]