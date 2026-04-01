# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        return self.helper(root, float('-inf'), float('inf'))
        
    def helper(self, node, low_bound, high_bound) -> bool:
        if not node:
            return True
        if node.val > low_bound and node.val < high_bound:
            return self.helper(node.left, low_bound, node.val) and self.helper(node.right, node.val, high_bound)
        else:
            return False
