# https://www.geeksforgeeks.org/number-children-given-node-n-ary-tree/?msclkid=e6841953d07a11ec9058788ebece05cf

class Node:
    def __init__(self, data = None):
        self.key = data
        self.child = []

def numberOfChildren(root, x):
    numChildren = 0

    if root is None:
        return 0

    q = []
    q.append(root)

    while len(q) > 0:
        n = len(q)

        while n > 0:
            p = q[0]
            q.pop(0)

            if p.key == x:
                numChildren = numChildren + len(p.child)
                return numChildren

            i = 0
            while i < len(p.child):
                q.append(p.child[i])
                i = i + 1
            n -= 1
    return numChildren

root = Node(20)
root.child.append(Node(2))
root.child.append(Node(34))
root.child.append(Node(50))
root.child.append(Node(60))
root.child.append(Node(70))

root.child[0].child.append(Node(15))
root.child[0].child.append(Node(20))

root.child[1].child.append(Node(30))

root.child[2].child.append(Node(40))
root.child[2].child.append(Node(100))
root.child[2].child.append(Node(20))

root.child[0].child[1].child.append(Node(25))
root.child[0].child[1].child.append(Node(50))

x = 2

print(numberOfChildren(root, x))