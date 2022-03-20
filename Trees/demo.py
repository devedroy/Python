class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

def leftView(root):
    if root is None:
        return
    print(root.data)
    leftView(root.left)

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
# root.left.left = Node(4)
root.right.right = Node(5)
root.right.right.right = Node(6)

# leftView(root)
print(height(root))