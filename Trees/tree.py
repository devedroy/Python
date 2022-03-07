from sympy import root


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(root):
    #LrR
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    #LRr
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

def preorder(root):
    #rLR
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# print(root.left.value)

# print(count_nodes(root))

#inorder LrR=4 2 5 1 3
inorder(root)