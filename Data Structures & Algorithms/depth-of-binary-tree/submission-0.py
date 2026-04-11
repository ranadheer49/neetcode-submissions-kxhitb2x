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
                return
            self.globalMax = max(self.globalMax, slate)    
            if node.left:
                dfs(node.left , slate + 1)
            if node.right:
                dfs(node.right, slate + 1)
            
        dfs(root,1)
        return self.globalMax                 
        