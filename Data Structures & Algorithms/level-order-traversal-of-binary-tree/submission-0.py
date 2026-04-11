# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        finalList = []
        if root is None:
            return []
        treeQueue = collections.deque()
        treeQueue.append(root)
        while len(treeQueue) > 0:
            count = len(treeQueue)
            tempList = []
            while count > 0:
                tempNode = treeQueue.popleft()
                tempList.append(tempNode.val)
                count -= 1
                if tempNode.left is not None:
                    treeQueue.append(tempNode.left)
                if tempNode.right is not None:
                    treeQueue.append(tempNode.right)

            finalList.append(tempList[:])

        return finalList    



        