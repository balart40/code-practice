# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        i = 1
        prev_even = curr_even = ListNode(-1)
        prev_odd = curr_odd = head
        while curr_odd:
            if i == 1:
                pass
            elif i % 2 == 0:
                curr_even.next = curr_odd
                curr_even = curr_even.next
            else:
                prev_odd.next = curr_odd
                prev_odd = prev_odd.next
            curr_odd = curr_odd.next
            i += 1
        curr_even.next = None
        prev_odd.next = prev_even.next
        return head