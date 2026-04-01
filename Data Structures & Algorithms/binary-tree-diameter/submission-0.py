# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            leftH = dfs(node.left)
            rightH = dfs(node.right)
            d = leftH + rightH
            self.diameter = max(self.diameter, d)
            return 1 + max(leftH, rightH)

        dfs(root)
        return self.diameter