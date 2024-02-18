# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr, carry = temp, 0
        while l1 or l2 or carry:
            t = carry
            if l1:
                t += l1.val
                l1=l1.next
            if l2:
                t += l2.val
                l2=l2.next
            carry, t = t//10, t%10
            curr.next = ListNode(t)
            curr = curr.next
        return temp.next
