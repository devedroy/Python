#https://www.geeksforgeeks.org/print-level-order-traversal-line-line/



class newNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    
    q = []
    q.append(root)


root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)

printLevelOrder(root)