"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def levelTraversal(node, level, lst):
            if node != None:
                if level == len(lst):
                    lst.append([])
                lst[level].append(node)
                if node.left != None:
                    levelTraversal(node.left, level+1, lst)
                if node.right != None:
                    levelTraversal(node.right, level+1, lst)

        level = list()
        levelTraversal(root, 0, level)
        for i in range(len(level)):
            for j in range(len(level[i])):
                if j+1 < len(level[i]):
                    level[i][j].next = level[i][j+1]
        return root