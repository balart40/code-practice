# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(0)
        temp = result.next = head
        # get number of nodes O(n)
        m = 0
        while temp != None:
            m += 1
            temp = temp.next
        # target node
        target = m - n + 1
        # case of one node only
        if m == 1 and n == 1:
            return None
        # case not removal
        if m == 1 and n == 0:
            return head
        # if requesting firt node
        if target == 1:
            return head.next
        # else
        i = 1
        prev_node = None
        while head != None:
            if i == 1:
                prev_node = head
            if i == target:
                #print "hit target"
                # if it was the last one
                if head.next ==  None:
                    prev_node.next = None
                    break
                elif head.next != None:
                    #print "hola"
                    prev_node.next = head.next
                    break
            i += 1
            prev_node = head
            head = head.next
        return result.next
