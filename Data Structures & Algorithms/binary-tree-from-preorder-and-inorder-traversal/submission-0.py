# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = 0
        self.idx_map = {val: i for i, val in enumerate(inorder)}

        return self.helper(self.pre_index, len(inorder)-1)
           

    def helper(self, in_left, in_right):
        if in_left > in_right:
            return None
    
        # pick current root from preorder
        root_val = preorder[self.pre_index]
        self.pre_index += 1
        
        root = TreeNode(root_val)
        
        # root splits inorder into left and right
        index = self.idx_map[root_val]
        
        # build subtrees recursively
        root.left = self.helper(in_left, index - 1)
        root.right = self.helper(index + 1, in_right)
        
        return root



