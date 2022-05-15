
class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def searchNodeinTree(root, value):
    if root is None:
        return False
    if root.value == value:
        return root
    return searchNodeinTree(root.left, value) or searchNodeinTree(root.right, value)

def levelOrderTraversal(root):
    if root is None:
        return
    queue = []
    res = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        # print(node.value, end=" ")
        res.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res[1:]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

searchVal = searchNodeinTree(root, 2)
print(levelOrderTraversal(searchVal))

