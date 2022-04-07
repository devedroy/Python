from itertools import permutations
N = int(input()) # len_arr 5 
M = int(input()) #mod 10
K = int(input()) #rand 30
arr = [int(x) for x in input().split()] # [10, 5, 3, 1, 3]

'''

'''

def solve(N,M,K,arr):
    perms = list(permutations(list(range(1,N+1))))
    for p in perms:
        avg_score = {0:0}
        score = M
        for i in range(1,N+1):
            avg_score[i] = (score//(i))*(M/(i))
            if avg_score[i] <= arr[p[i-1] - 1]:
                score = score+M
                print(score, avg_score[i], arr[p[i-1]])
            else:
                continue
    
    if score/N != (K/N):
        return "NO"
    return "YES"

print(solve(N,M,K,arr))