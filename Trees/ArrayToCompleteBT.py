


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = newNode(arr[i])
        root = temp
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    inorder(root)