# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    counter = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        res = self.helper(root, k)
        return res
    
    def helper(self, node, k):
        if not node:
            return None
        val = self.helper(node.left, k)
        if val is not None:
            return val
        self.counter += 1
        if self.counter == k:
            return node.val
        return self.helper(node.right, k)