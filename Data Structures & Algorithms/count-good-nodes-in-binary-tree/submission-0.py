# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, curr_h):
            if not node:
                return 
            if curr_h <= node.val:
                self.res += 1
            curr_h = max(curr_h, node.val)
            dfs(node.left, curr_h)
            dfs(node.right, curr_h)
        dfs(root, -101)
        return self.res