
def mergeDicts(d1, d2):
    res = {}
    
    for k,v in d2:
        if k in d1.keys():
            d1[k] = v
        else:
            d1[k+"new"] = v
    return d1

d1 = {"cap":97,
"book":8,
"pen":12}
d2 = {"pen":18,
"brush":16,
"eraser":110}

print(d1)
print(d2)
print(mergeDicts(d1, d2))