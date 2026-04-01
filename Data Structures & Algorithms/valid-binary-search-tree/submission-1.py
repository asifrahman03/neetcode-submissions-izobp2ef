# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_m, right_m):
            if not node:
                return True
            if node.val > left_m and node.val < right_m:
                return dfs(node.left, left_m, node.val) and dfs(node.right, node.val, right_m)
            return False
        return dfs(root, float('-inf'), float('inf'))