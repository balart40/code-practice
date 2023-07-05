# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tempNode = None
        s = ""
        # we will read while inverting
        i = 0
        while head != None:
            s += str(head.val)
            head = head.next

        return s == s[::-1]