#https://www.techiedelight.com/levenshtein-distance-edit-distance-problem/
#https://www.geeksforgeeks.org/edit-distance-dp-5/

def levenshteinDistance(X, m, Y, n):
    if m == 0:
        return n
    if n == 0:
        return m

    cost = 0 if X[m-1] == Y[n-1] else 1

    return min(levenshteinDistance(X, m - 1, Y, n) + 1, levenshteinDistance(X, m, Y, n - 1) + 1, levenshteinDistance(X, m - 1, Y, n - 1) + cost)
if __name__ == '__main__':
    x = 'kitten'
    y = 'sitting'

    print(levenshteinDistance(x, len(x) y, len(y)))

#https://www.techiedelight.com/data-structures-and-algorithms-problems/