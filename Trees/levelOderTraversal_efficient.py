#https://www.geeksforgeeks.org/print-level-order-traversal-line-line/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(70)
root.right.right.right = Node(80)

levelOrderTraversal(root)