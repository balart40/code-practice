# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2:
            return list2
        if list2 == None and list1:
            return list1
        result = ListNode(0)
        curr = result
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                if list1 == None and list2:
                    curr.next = list2
                    break

            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                if list2 == None and list1:
                    curr.next = list1
                    break
        return result.next
