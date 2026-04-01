# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.pathAdd(root)
        return self.res
    
    def pathAdd(self, node) -> int:
        if not node:
            return 0
        leftN = self.pathAdd(node.left)
        rightN = self.pathAdd(node.right)
        self.res = max(self.res, node.val + max(0, leftN) + max(0, rightN))
        return node.val + max(0, leftN, rightN)

