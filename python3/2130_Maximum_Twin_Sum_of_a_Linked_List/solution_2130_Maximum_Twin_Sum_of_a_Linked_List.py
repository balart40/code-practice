# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head: return 0
        nums = []
        result = 0
        while head:
            nums.append(head.val)
            head = head.next
        while nums:
            result = max(result, nums.pop()+nums.pop(0))
        return result