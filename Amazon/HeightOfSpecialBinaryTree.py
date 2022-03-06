class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isLeaf(node):
    return node.left and node.left.right == node and \
              node.right and node.right.left == node

def maxDepth(node):
    if (node == None):
        return 0

    if(isLeaf(node)):
        return 1

    return max(maxDepth(node.left), maxDepth(node.right)) + 1

if __name__ == '__main__':
    root = newNode(1)

    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.left.left.left = newNode(6)

    L1 = root.left.left.left
    L2 = root.left.right
    L3 = root.right

    L1.right = L2
    L2.right = L3
    L3.right = L1

    L3.left = L2
    L2.left = L1
    L1.left = L3

    print("Height of tree is: " + str(maxDepth(root)))