'''
    0
    24
    6810
    12141618
    2022242628
'''
p = 0
for i in range(1, 6):
    for j in range(0, i):
        print(p, end = '')
        p += 2
    print()