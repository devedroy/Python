from prometheus_client import Counter


from collections import Counter

def dupChar(sent):
    wc = Counter(sent)
    # print(wc)
    j = -1

    for i in wc.values():
       j += 1
       if(i > 1):
           print(wc.keys()[j])

sent = "deved"
dupChar(sent)