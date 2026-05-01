# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p,q = list1,list2
        newhead = None
        
        if not p : return q
        if not q : return p

        if p.val <= q.val:
            newhead = p
            p = p.next
        else:
            newhead = q
            q = q.next
        
        r = newhead

        while p and q:
            if p.val<=q.val:
                r.next = p
                r = r.next
                p = p.next
            else:
                r.next = q
                r = r.next
                q = q.next
            
        if not p: r.next = q
        if not q: r.next = p

        return newhead