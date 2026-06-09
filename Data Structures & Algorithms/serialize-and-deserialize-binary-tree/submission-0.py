# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def serializeTree(current):
            if not current:
                return 'N'
            return str(current.val) + "," + serializeTree(current.left) + "," + serializeTree(current.right)
        return serializeTree(root)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def deserializeTree(vals, idx):
            if vals[idx] == None:
                return (None, idx+1)
            current = TreeNode(vals[idx])
            current.left, right_idx = deserializeTree(vals, idx + 1)
            current.right, next_idx = deserializeTree(vals, right_idx)
            return (current, next_idx)
        vals = data.split(',')
        for i, val in enumerate(vals):
            if val == "N":
                vals[i] = None
            else:
                vals[i] = int(val)
        root, _ = deserializeTree(vals, 0)
        return root
        
