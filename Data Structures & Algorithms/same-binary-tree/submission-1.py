# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # same_tree = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(curr_p, curr_q):
            if not curr_p and not curr_q:
                return True
            if curr_p and not curr_q:
                return False
            if not curr_p and curr_q:
                return False
            if curr_p.val != curr_q.val:
                return False
            return dfs(curr_p.left, curr_q.left) and dfs(curr_p.right, curr_q.right)
            
        return dfs(p, q)