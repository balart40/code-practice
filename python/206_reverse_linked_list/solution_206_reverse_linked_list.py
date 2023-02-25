# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        if head ==  None:
            return head
        while head != None:
            stack.insert(0, head)
            head = head.next
        for i in range(len(stack)):
            if i < len(stack) - 1:
                stack[i].next = stack[i + 1]
        stack[-1].next = None
        return stack[0]

