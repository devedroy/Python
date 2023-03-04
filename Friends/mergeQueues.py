def mergeQues(q1, q2): 
    #1,4,2,5,3,6
    n = len(q1) + len(q2)
    i = 0
    res = []

    while q1 and q2:
        if i % 2 == 0:
            q1e = q1.pop(0)
            res.append(q1e)
        else:
            q2e = q2.pop(0)
            res.append(q2e)

        i += 1
    
    if q1:
        res.extend(q1)
    if q2:
        res.extend(q2)
    
    return res

q1 = [1,2,3]
q2 = [4,5,6,7]


print(mergeQues(q1=q1, q2=q2))