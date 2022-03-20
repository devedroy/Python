class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 0:
        print(root.data, end=" ")
    elif level > 0:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def levelOrderTraversal(root):
    if root is None:
        return

    h = height(root)
    for i in range(h):
        printGivenLevel(root, i)

    
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
root.right.right.right = Node(80)

levelOrderTraversal(root)