# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSideElements = []

        if not root:
            return []

        levelQueue = deque()
        levelQueue.append(root)

        while len(levelQueue) > 0:
            levelNodeCount = len(levelQueue)
            rightSideElements.append(levelQueue[-1].val)


            for _ in range(levelNodeCount):
                tempNode = levelQueue.popleft()
                if tempNode.left:
                    levelQueue.append(tempNode.left)
                if tempNode.right:
                    levelQueue.append(tempNode.right)

        return rightSideElements
        