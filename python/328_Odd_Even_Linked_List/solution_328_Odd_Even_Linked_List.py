# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        # > 1 linked list
        result = head
        first_even = curr_even = curr_odd = None
        i = 1
        while head:
            # if odd
            if i % 2 != 0:
                if i == 1:
                    curr_odd = head
                else:
                    curr_odd.next = head
                    curr_odd = curr_odd.next
            # if even
            else:
                if i == 2:
                    first_even = head
                    curr_even = head
                else:
                    curr_even.next = head
                    curr_even = curr_even.next
            i += 1
            head = head.next
        curr_even.next = None
        curr_odd.next = first_even
        return result