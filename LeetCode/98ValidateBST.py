# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, cur_min, cur_max):
            if not node:
                return True
            if node.val <= cur_min or node.val >= cur_max:
                return False
            left = helper(node.left, cur_min, node.val)
            right = helper(node.right, node.val, cur_max)
            return left and right
        return helper(root, float('-inf'), float('inf'))