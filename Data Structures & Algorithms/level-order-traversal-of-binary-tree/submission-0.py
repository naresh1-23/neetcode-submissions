# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.result = []

    def traverse(self, node, level):
        if not node:
            return

        if len(self.result) == level:
            self.result.append([])

        self.result[level].append(node.val)

        self.traverse(node.left, level + 1)
        self.traverse(node.right, level + 1)
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0)
        return self.result
        