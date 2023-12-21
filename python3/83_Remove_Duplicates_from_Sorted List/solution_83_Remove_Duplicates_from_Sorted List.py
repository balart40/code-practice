# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        past = head
        curr = head.next
        while curr:
            if past.val != curr.val:
                past.next = curr
                past =  past.next
            curr = curr.next
        if past.next and past.val == past.next.val:
            past.next = None
        return head