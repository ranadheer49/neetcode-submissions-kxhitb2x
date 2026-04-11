# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.globalDia = 0

        def dfs(node) -> int:

            if node.left is None and node.right is None:
                return 0

            localDia = 0
            lh,rh = 0, 0
            if node.left:
                lh = dfs(node.left)
                localDia += lh + 1
            if node.right:
                rh = dfs(node.right)
                localDia += rh + 1

            self.globalDia = max(self.globalDia, localDia)

            return max(lh,rh) + 1

        dfs(root)
        return self.globalDia            
        