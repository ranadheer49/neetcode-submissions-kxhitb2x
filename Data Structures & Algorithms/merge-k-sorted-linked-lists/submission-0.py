# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#  get all the first nodes into a minheap
#  we pop the top node, then replace the next node of the top node
#  repeat this untill heap becomes empty 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i , node))

        finalNode = ListNode(0)
        curr = finalNode

        while minHeap:
            _,i,node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap,(node.next.val, i, node.next))


        return finalNode.next        


