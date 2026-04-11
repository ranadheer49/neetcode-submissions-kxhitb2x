# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxHeight = 0

        if not root:
            return 0

        def dfs(node):
                # base case
            if not node:
                return 0
            lh ,rh  =0 , 0
            lh = 1 + dfs(node.left)  
            rh = 1+ dfs (node.right)  
            return max(lh , rh)
        return dfs(root)    
            
 


