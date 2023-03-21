# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Floyds cycle detection
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        slow = fast = head
        while fast != None and fast.next != None:
            fast =  fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False