# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.max_val = float('-inf')
        self.result = 0


    def traverse(self, root, max_val):
        if not root:
            return
        if root.val>=max_val:
            self.max_val = root.val
            self.result+=1
        self.traverse(root.left, self.max_val)
        self.max_val = max_val if root.val<max_val else root.val
        self.traverse(root.right, self.max_val)

    def goodNodes(self, root: TreeNode) -> int:
        self.traverse(root, self.max_val)
        return self.result
        