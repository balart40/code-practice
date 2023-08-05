class Solution(object):
    def isCousins(self, root, x, y):
        d = dict()

        def dfs(node, depth, parent):
            if not node:
                return
            d[node.val] = [depth, parent.val if parent else None]
            if node.left:
                dfs(node.left, depth + 1, node)
            if node.right:
                dfs(node.right, depth + 1, node)

        dfs(root, 0, None)
        return d[x][0] == d[y][0] and d[x][1] != d[y][1]