# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        finalList = []

        if root is None:
            return []

        nodeQue = deque()
        nodeQue.append(root)
        switch = 0 

        while len(nodeQue) > 0:
            tempList = []
            for _ in range(len(nodeQue)):
                tempNode = nodeQue.popleft()
                tempList.append(tempNode.val)
                if tempNode.left:
                    nodeQue.append(tempNode.left)
                  
                if tempNode.right:
                    nodeQue.append(tempNode.right)

            if switch:
                tempList.reverse()
                switch = 0
            else:
                switch = 1    

            finalList.append(tempList[:])


        return finalList    



        