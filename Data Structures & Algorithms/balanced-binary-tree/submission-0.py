# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True
            leftH = dfs(node.left)
            rightH = dfs(node.right)
            if abs(leftH - rightH) > 1:
                self.balanced = False
                return self.balanced
            return 1 + max(leftH, rightH)
        dfs(root)
        return self.balanced