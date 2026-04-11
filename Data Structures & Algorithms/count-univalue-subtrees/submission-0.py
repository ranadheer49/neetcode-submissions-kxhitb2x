# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.univalCount = 0
        if root is None:
            return 0
        def dfs(node):
            if node is None:
                self.univalCount += 1
                return True
            isUniVal = True
            if node.left:
                lb = dfs(node.left)
                if node.left.val != node.val or not lb:
                    isUniVal = False
            if node.right:
                rb = dfs(node.right) 
                if node.right.val != node.val or not rb:
                    isUniVal = False
            if isUniVal:
                self.univalCount += 1
            return   isUniVal  
        dfs(root)
        return self.univalCount    

