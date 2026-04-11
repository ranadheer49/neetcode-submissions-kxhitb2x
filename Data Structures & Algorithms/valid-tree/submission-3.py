class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = [-1] * n
        parent = [-1] * n
        adjLi = [[] for _ in range(n)]

        for u,v in edges:
            adjLi[u].append(v)
            adjLi[v].append(u)

        def dfs(node):
            visited[node] = 1
            for i in adjLi[node]:
                if visited[i] == -1:
                    parent[i] = node
                    if dfs(i):
                        return True
                else:
                    if parent[node] != i:
                        return True    


            return False

        component = 0
        for i in range(n):
            if visited[i] == -1:
                component += 1
                if component > 1 or dfs(i):
                    return False

        return True                                 



        