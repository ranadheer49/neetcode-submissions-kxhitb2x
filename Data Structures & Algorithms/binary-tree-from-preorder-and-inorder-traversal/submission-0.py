# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = {}

        for i in range(len(inorder)):
            hmap[inorder[i]] = i

        def helper(p,startP,endP,i,startI,endI):

            if startP > endP:
                return None
            if startP == endP:
                return TreeNode(p[startP])

            currNode = TreeNode(p[startP])
            currIndex = hmap[p[startP]]
            nums = currIndex - startI

            currNode.left = helper(p,startP+1,startP + nums ,
                                    i,startI,currIndex -1)
            currNode.right = helper(p,startP + nums +1, endP,
                                    i, currIndex+1, endI)      

            return currNode

        return helper(preorder,0,len(preorder)-1, inorder, 0, len(inorder) - 1)                                  
        