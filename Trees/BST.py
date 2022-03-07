

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

def search(node, key):
    if node is None:
        return node
    if node.data == key:
        return node
    if node.data < key:
        return search(node.right, key)
    if node.data > key:
        return search(node.left, key)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, key):
    if node is None:
        return node
    if key < node.data:
        node.left = delete(node.left, key)
    elif key > node.data:
        node.right = delete(node.right, key)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        temp = minValueNode(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)
    return node

root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)

ok = search(root, 30)
print(ok)

o = delete(root, 30)

ok = search(root, 30)
print(ok)