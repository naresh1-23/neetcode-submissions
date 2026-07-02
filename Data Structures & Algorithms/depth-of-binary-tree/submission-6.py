# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxPath = 0
        self.tempMaxPath = 0


    def maxLength(self, root):
        if not root:
            return  0
        return 1 + max(
        self.maxLength(root.left),
        self.maxLength(root.right)
    )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxLength(root)
        