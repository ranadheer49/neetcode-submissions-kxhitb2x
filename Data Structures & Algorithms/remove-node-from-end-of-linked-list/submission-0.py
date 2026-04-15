# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #  find length of the linked list
        #  cal the element position from the start (len(linkedlist) - n)
        #  traverse from start and delete the node
        start = ListNode(0,head)
        left = start
        right = head

        while n:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return start.next        