class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        countRow = []
        for idx, vals in enumerate(mat):
            count = sum(vals)
            countRow.append([idx, count])
        countRow.sort(key = lambda x: x[1])
        res = []
        for i in range(k):
            res.append(countRow[i][0])
        return res