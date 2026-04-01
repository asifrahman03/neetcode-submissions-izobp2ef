# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_imap = {}
        for i, val in enumerate(inorder):
            node_imap[val] = i
        self.i = 0
        def dfs(l, r):
            if l >= r:
                return None
            node = TreeNode(preorder[self.i])
            self.i += 1
            index_inorder = node_imap[node.val]
            node.left = dfs(l, index_inorder)
            node.right = dfs(index_inorder+1, r)
            return node
        return dfs(0, len(preorder))

        
