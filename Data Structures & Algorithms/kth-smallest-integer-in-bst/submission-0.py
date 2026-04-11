# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.globalList = []

        def dfs(node):
            if node.left is None and node.right is None:
                self.globalList.append(node.val)
                return

            if node.left:
                dfs(node.left)
            self.globalList.append(node.val)    
            if node.right:
                dfs(node.right)
   
            return  
        dfs(root)
        return self.globalList[k-1]            
        