# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def delete_node_rec(node, key):
            if not node: return None
            if key  < node.val:
                node.left = delete_node_rec(node.left, key)
            elif key > node.val:
                node.right = delete_node_rec(node.right, key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                else:
                    temp_node = node.right
                    while temp_node.left:
                        temp_node = temp_node.left
                    node.val = temp_node.val
                    node.right = delete_node_rec(node.right, temp_node.val)
            return node
        return delete_node_rec(root, key)