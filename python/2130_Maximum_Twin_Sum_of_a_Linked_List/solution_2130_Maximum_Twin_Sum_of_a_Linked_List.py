# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        """
        if head == None:
            return head
        elif head.next == None:
            return head.val

        n = 0
        curr = head
        reversed_vals = []

        while curr:
            n += 1
            reversed_vals.insert(0, curr.val)
            curr = curr.next

        curr_sum = 0
        max_sum = head.val
        i = 0
        while 0 <= i <= (n / 2) - 1:
            curr_sum = head.val + reversed_vals[0]
            max_sum = max(curr_sum, max_sum)
            reversed_vals.pop(0)
            head = head.next
            i += 1
        return max_sum
        """
        slow = fast = head
        prev =  None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            # reverse first half which will return prev
            slow.next = prev
            prev = slow
            slow = temp

        max_sum = 0
        while slow and prev:
            max_sum = max(max_sum, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return max_sum