# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node):
            if node.left is None and node.right is None:
                return

            currNode = node
            currNode.left , currNode.right = currNode.right, currNode.left
            if currNode.left:
                dfs(currNode.left)
            if currNode.right:    
                dfs(currNode.right)

            return currNode

        dfs(root)
        return root        
        