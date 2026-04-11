class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = [-1] * n
        parent = [-1] * n
        adjLi = [[] for _ in range(n)]

        for u,v in edges:
            adjLi[u].append(v)
            adjLi[v].append(u)

        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 1

            while q :
                cur = q.popleft()
                
                
                for i in adjLi[cur]:
                    
                    if visited[i] == -1:
                        parent[i] = cur
                        visited[i] = 1
                        q.append(i)
                    else: 
                        if parent[cur] != i:
                            return True   

            return False

        component = 0
        for i in range(n):
            if visited[i] == -1:
                component += 1
                if component > 1 or bfs(i):
                    return False

        return True                                 



        