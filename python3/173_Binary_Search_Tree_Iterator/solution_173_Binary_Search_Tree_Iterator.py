# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.result = []
        self.in_order(root)

    def next(self) -> int:
        return self.result.pop(0)


    def hasNext(self) -> bool:
        return not self.result == []

    def in_order(self, node):
        if not node: return
        self.in_order(node.left)
        self.result.append(node.val)
        self.in_order(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()