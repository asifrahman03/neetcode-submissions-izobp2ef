# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            sze = len(q)
            for i in range(sze):
                node = q.popleft()
                if i == sze-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
                # res.append(node.val)
            #     if node.right:
            #         q.append(node.right)
            #         if not (node.right.left and node.right.right):
            #             if node.left.left:
            #                 q.append(node.left.left)
            #             if node.left.right:
            #                 q.append(node.left.right)
            # elif node.left:
            #     q.append(node.left)
            
        # def dfs(node):
        #     if not node:
        #         return res
        #     res.append(node.val)
        #     if not node.right:
        #         return dfs(node.left)
        #     else:
        #         return dfs(node.right)
        # return dfs(root)