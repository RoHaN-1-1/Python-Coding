#Remove Nth Node from End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x = ListNode(0, head)
        y = x

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            y = y.next
        
        y.next = y.next.next

        return x.next