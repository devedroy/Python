
#https://www.tutorialspoint.com/program-to-find-sibling-value-of-a-binary-tree-node-in-python

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def util(root, k, ans):

class Solution:
    def solve(self, root, k):
        ans = []
        util(root, k, ans)
        return ans[0]

root = TreeNode(6)
root.left = TreeNode(4)
root.right = TreeNode(10)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)

