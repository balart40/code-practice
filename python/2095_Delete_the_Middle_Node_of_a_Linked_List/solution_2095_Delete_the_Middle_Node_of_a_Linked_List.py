# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pass1 = pass2 = head
        c1 = 0

        while pass1:
            pass1 = pass1.next
            c1 += 1


        n = (c1 / 2)
        c2 = 0
        prev_pass2 = None

        while pass2:
            # found middle one
            if c2 == n:
                # not previous
                if not prev_pass2:
                    # there is next
                    if pass2.next:
                        head = pass2.next
                        pass2.next = None
                    else:
                        head = None
                # previous
                else:
                    # there is next
                    if pass2.next:
                        prev_pass2.next = pass2.next
                        pass2.next = None
                    else:
                        prev_pass2.next = None
                break
            else:
                prev_pass2 = pass2
                pass2 = pass2.next
                c2 += 1
        return head