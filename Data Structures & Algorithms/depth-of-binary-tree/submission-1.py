# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.globalMax = 0
        def dfs(node,slate):
            if not node:
                self.globalMax = max(self.globalMax, slate) 
                return
               
            dfs(node.left , slate + 1)
            dfs(node.right, slate + 1)
            
        dfs(root,0)
        return self.globalMax                 
        