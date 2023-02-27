# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        curr = result
        summ = 0
        a = 0
        b = 0
        while l1 or l2:
            if l1 == None:
                a = 0
            else:
                a = l1.val
                l1 = l1.next
            if l2 == None:
                b = 0
            else:
                b = l2.val
                l2 = l2.next
            summ = a + b + carry
            carry = 1 if summ > 9 else 0
            if carry == 1:
                summ = summ % 10
            curr.next = ListNode(summ)
            curr = curr.next
        if carry == 1:
            curr.next = ListNode(1)
        return result.next
