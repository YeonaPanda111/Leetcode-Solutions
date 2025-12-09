# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head
        l=[]
        maxi=0
        
        while (fast):
            l.append(slow.val)
            slow=slow.next
            fast=fast.next.next

        while(slow):
            t=0
            t=slow.val+l.pop()

            if maxi<t:
                maxi=t
            slow=slow.next
        return maxi
