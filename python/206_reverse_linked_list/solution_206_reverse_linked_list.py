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
        """
        # if head is None or is just one node return head
        if head == None or head.next == None:
            return head
        # from here we are 2 or more
        result = ListNode(0)
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node