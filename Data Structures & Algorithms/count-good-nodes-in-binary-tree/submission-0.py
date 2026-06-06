# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def findGoodNodes(maxVal, current):
            if not current:
                return 0
            result = 0
            if current.val >= maxVal:
                result += 1
                maxVal = current.val

            rightRes = findGoodNodes(maxVal, current.right)
            leftRes = findGoodNodes(maxVal, current.left)
            return rightRes + leftRes + result
        return findGoodNodes(-101, root)

        