# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        currLevel = 0

        q.append(root)
        while q:
            len_q = len(q)
            res.append([])

            for i in range(len_q):
                node = q.popleft()
                res[currLevel].append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            currLevel+=1
        return res
