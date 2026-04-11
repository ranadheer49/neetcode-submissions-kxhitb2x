"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newGraph = {}
        if not node:
            return None
        newGraph[node] = Node(node.val)
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in newGraph:
                    newGraph[nei] = Node(nei.val)
                    q.append(nei)
                newGraph[cur].neighbors.append(newGraph[nei]) 

        return newGraph[node]               