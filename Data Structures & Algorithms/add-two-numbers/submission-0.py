# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            res = 0 + carry

            if l1:
                res += l1.val
                l1 = l1.next
            
            if l2:
                res += l2.val
                l2 = l2.next

            carry = res//10
            res %= 10
            cur.next = ListNode(res)
            cur = cur.next

        return dummy.next