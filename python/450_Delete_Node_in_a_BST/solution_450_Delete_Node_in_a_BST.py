# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def delete_node_recursive(node):
            if node == None:
                return None
            if node.val == key:
                if node.left:
                    node_left_right_most = node.left
                    while node_left_right_most.right:
                        node_left_right_most = node_left_right_most.right
                    node_left_right_most.right = node.right
                    return node.left
                else:
                    return node.right
            elif node.val < key:
                node.right = delete_node_recursive(node.right)
            else:
                node.left = delete_node_recursive(node.left)
            return node
        return delete_node_recursive(root)