
from lib2to3.pytree import Node
from pip import main
from sympy import root

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findMinElement(inorder, start, end):
   minIndex = start
   for i in range(start + 1, end + 1):
       if inorder[i] < inorder[minIndex]:
           minIndex = i
   return minIndex

def constructTree(inorder, start, end):
    if start > end:
        return None
    index = findMinElement(inorder, start, end)

    root = Node(inorder[index])
    root.left = constructTree(inorder, start, index - 1)
    root.right = constructTree(inorder, index + 1, end)
    return root

def inorderTraversal(root):
    if root is None:
        return
    inorderTraversal(root.left)
    print(root.data, end = " ")
    inorderTraversal(root.right)

if __name__ == '__main__':
    
    inorder = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]

    root = constructTree(inorder, 0, len(inorder) - 1)
    print('Inorder traversal of constructed tree:', end=' ')
    inorderTraversal(root)
