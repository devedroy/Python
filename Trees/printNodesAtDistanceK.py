class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printKDist(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    printKDist(root.left, k-1)
    printKDist(root.right, k-1)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
root.right.right.right = Node(80)

printKDist(root, 2)