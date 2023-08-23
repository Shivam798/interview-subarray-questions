class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def merge_list(l1,l2):
    dummy=ListNode(0)
    cur=dummy
    while l1 and l2:
        if l1.val>l2.val:
            cur.next=l2
            l2=l2.next
        else:
            cur.next=l1
            l1=l1.next
        cur=cur.next
    if l1:
        cur.next=l1
    if l2:
        cur.next=l2
    return dummy.next

def Reverse(node):
    prev=None
    cur=node
    while cur:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next
    return prev


def Cycle_detect_start(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    # slow==fast mean cycle exist
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next.next
    return slow.val
    

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(4)

l2=ListNode(1)
l2.next=ListNode(3)
l2.next.next=ListNode(4)

# merge_head=merge_list(l1,l2)

# while merge_head:
#     print(merge_head.val)
#     merge_head=merge_head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next

print(Cycle_detect_start(head))