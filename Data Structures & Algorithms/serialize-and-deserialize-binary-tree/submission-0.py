# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        if not root:
            return ""
        dfs(root)
        return ",".join(res)
        

    # Decodes your encoded data to tree.
    index = 0
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) < 1:
            return None
        split_s = data.split(',')
        root = None
        def dfs(str_val, index):
            if str_val == "N":
                return None
            node = TreeNode(int(str_val))
            self.index += 1
            node.left = dfs(split_s[self.index], self.index)
            self.index += 1
            node.right = dfs(split_s[self.index], self.index)
            return node
        return dfs(split_s[self.index], self.index)

