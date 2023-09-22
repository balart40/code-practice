/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const result = new ListNode(0);
    let currNode = result;
    while(list1 || list2) {
        if(list1 && list2) {
            if(list1.val <= list2.val) {
                currNode.next = list1
                list1 = list1.next
            } else {
                currNode.next = list2
                list2 = list2.next
            }
        } else if (!list1 && list2) {
            currNode.next = list2
            list2 = list2.next
        } else if (!list2 && list1) {
            currNode.next = list1
            list1 = list1.next
        }
        currNode = currNode.next
    }
    return result.next;
};