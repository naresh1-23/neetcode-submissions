class Solution:

    def __init__(self):
        self.result = []

    def traverseRight(self, root: Optional[TreeNode], level: int):
        if not root:
            return
        print(root.val,level, self.result)

        if level == len(self.result):
            self.result.append(root.val)

        self.traverseRight(root.right, level + 1)

        self.traverseRight(root.left, level + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.traverseRight(root, 0)
        return self.result