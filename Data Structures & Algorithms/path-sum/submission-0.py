# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.pathExists = False
        if not root:
            return False
        def dfs(node, target):
            if node.left is None and node.right is  None: 
                if  target == node.val:
                    self.pathExists = True
                return             
            if node.left:
                dfs(node.left,target - node.val)
            if node.right:
                dfs(node.right,target - node.val)

        dfs(root,targetSum)
        return self.pathExists            

        