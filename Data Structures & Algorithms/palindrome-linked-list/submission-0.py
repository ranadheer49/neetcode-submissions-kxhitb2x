# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        prev,fast,slow, curr = None,head,head,head

        if not fast.next or not fast.next.next:
            if not fast.next:
                return True
            elif not fast.next.next:
                return fast.next.val == fast.val    

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            curr.next = prev
            prev = curr
            curr = slow

        right = slow.next
        slow.next = prev
        if fast.next is None:
            slow =slow.next

        while slow.next and right.next:
            if slow.val != right.val:
                return False

            slow =slow.next
            right = right.next

        return True        

        