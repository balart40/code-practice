# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = dict()
        while headA or headB:
            if headA != None:
                if seen.get(headA, None) == None:
                    seen[headA] = headA
                    headA = headA.next
                else:
                    return headA
            if headB != None:
                if seen.get(headB, None) == None:
                    seen[headB] = headB
                    headB = headB.next
                else:
                    return headB
        return None