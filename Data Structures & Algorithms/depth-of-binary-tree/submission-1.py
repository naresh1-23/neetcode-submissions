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
            if self.maxPath < self.tempMaxPath:
                self.maxPath = self.tempMaxPath
            return 
        self.tempMaxPath+=1
        print(root.val, self.tempMaxPath)
        self.maxLength(root.left)
        self.maxLength(root.right)
        self.tempMaxPath-=1
        root.left, root.right = root.right, root.left

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxLength(root)
        return self.maxPath
        