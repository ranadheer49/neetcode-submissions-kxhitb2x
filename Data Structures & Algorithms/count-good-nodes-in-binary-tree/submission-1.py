# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        min = float('-inf')

        def dfs(min,node):
            if not node:
                return

            if node.val >= min:
                count[0] += 1
                min = node.val

            dfs(max(node.val,min),node.left)  
            dfs(max(node.val,min), node.right)
            return 

        dfs(min,root) 
        return count[0]   
