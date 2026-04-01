# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def trav(node):
            if not node:
                return
            left_t = trav(node.left)
            if left_t is not None:
                return left_t
            else:
                self.count += 1
                if self.count == k:
                    return node
            return trav(node.right)
        return trav(root).val
