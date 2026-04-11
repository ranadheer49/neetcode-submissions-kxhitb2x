class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #  build an adjacency list
        aj = [[] for _ in range(n)]
        for u,v in edges:
            aj[u].append(v)
            aj[v].append(u)
        visited = [-1] * n
        #  dfs
        def dfs(node):
            
            for li in aj[node]:
                if visited[li] == -1:
                    visited[li] = 1
                    dfs(li)


        #  outer loop
        components = 0
        for i in range(n):
            if visited[i] == -1:
                visited[i] = 1
                
                dfs(i)
                components +=1

        return components

        