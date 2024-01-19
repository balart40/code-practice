# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m, i = 0, 0
        curr = head
        while curr:
            m += 1
            curr = curr.next
        if m == 1: return None
        if m  == n: return head.next
        curr = head
        while curr:
            if i == m - n - 1:
                if curr.next.next != None:
                    curr.next = curr.next.next
                else:
                    curr.next = None
                break
            i += 1
            curr =  curr.next
        return head