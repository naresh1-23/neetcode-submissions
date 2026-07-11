# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxLength(self, root):
        if not root:
            return 0

        return 1 + max(
            self.maxLength(root.left),
            self.maxLength(root.right)
        )

    def checkHeight(self, root):
        if not root:
            return True

        left = self.maxLength(root.left)
        right = self.maxLength(root.right)

        if abs(left - right) > 1:
            return False

        return self.checkHeight(root.left) and self.checkHeight(root.right)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.checkHeight(root)
        