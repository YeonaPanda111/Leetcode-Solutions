# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        i=head
        p=i
        while i and i.next:
            if i.next.val!=i.val:
                p.next=i.next
                p=p.next
            i=i.next
        p.next=None
            
        return head 
