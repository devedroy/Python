front = []
back = []
def push_back():
    if back:
        return
    while front:
        back.append(front.pop())
def dequeue():
    push_back()
    back.pop()
def enqueue(item):
    front.append(item)
for i in range(int(input())):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        enqueue(inp[1])
    elif inp[0] == 2:
        dequeue()
    else:
        