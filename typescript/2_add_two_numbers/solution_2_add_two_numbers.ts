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

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const result = new ListNode(0)
    let currNode = result;
    let carry = 0
    while( l1 || l2) {
        let a = l1 ? l1.val : 0
        let b = l2 ? l2.val : 0
        let le_sum = a + b + carry
        carry = le_sum >=10 ? 1 : 0
        le_sum = le_sum % 10
        currNode.next = new ListNode(le_sum)
        currNode = currNode.next
        l1 = l1 ? l1.next : null
        l2 = l2 ? l2.next : null
    }
    if(carry != 0) {
        currNode.next = new ListNode(1)
    }
    return result.next;
};