# Definition for a binary search tree node
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to get the next greater element of a target in the binary search tree
def getNextGreaterElement(root, target):
    # To store the values of the binary search tree

    values = []

    def getNextGreaterElementRec(node, k):
        if node == None:
            return
        if node.val > k:
            heapq.heappush(values, node.val)
        getNextGreaterElementRec(node.left, k)
        getNextGreaterElementRec(node.right, k)

    getNextGreaterElementRec(root, target)
    result = heapq.heappop(values)
    return result

# Driver code
if __name__ == '__main__':
    # Construct the binary search tree
    """
          5
        /   \
        3	 7
       / \ /  \
     2   4 6   8
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # Target element to find the next greater element of
    target = 4

    # Function call
    nextGreaterElement = getNextGreaterElement(root, target)

    # Print the result
    if nextGreaterElement == -1:
        print "The next greater element of " + str(target) + " is not found"
    else:
        print "The next greater element of " + str(target) + " is  " + str(nextGreaterElement)
