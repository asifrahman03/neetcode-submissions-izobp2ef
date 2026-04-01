# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        def dfs(node):
            if not node:
                return
            heapq.heappush(vals, -node.val)
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        c = len(vals)
        while c != k:
            heapq.heappop(vals)
            c -= 1
        
        return -vals[0]