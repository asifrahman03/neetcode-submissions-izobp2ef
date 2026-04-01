# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        self.tree = ""
        def dfs(node):
            if not node:
                self.tree += 'N,'
                return
            self.tree += str(node.val) + ','
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        res = self.tree[:-1]
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        new_l = data.split(',')
        self.i = 0
        def dfs():
            if new_l[self.i] == 'N':
                self.i += 1
                return None
            val = int(new_l[self.i])
            node = TreeNode(val)
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
                
        return dfs()