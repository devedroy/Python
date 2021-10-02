S = int(input())
E = int(input())
W = int(input())

while S <= E:
    print(S,"\t",(S - 32)*5//9)
    S += W