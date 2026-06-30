# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def preorder(self, root):
        if not root:
            return

        self.preorder(root.left)
        self.preorder(root.right)
        root.left, root.right = root.right, root.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.preorder(root)
        return root
        