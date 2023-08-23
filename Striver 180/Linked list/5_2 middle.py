# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        cur=head
        while cur :
            cur=cur.next
            length+=1
        mid=length//2
        cur2=head
        while cur2 and mid:
            cur2=cur2.next
            mid-=1
        return cur2