class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #  build an adjacency list
        ajl = [[] for _ in range(n)]
        for u,v in edges:
            ajl[u].append(v)
            ajl[v].append(u)

        visited = [-1]*n 


        #  bfs/ dfs
        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 1
            while q:
                c = q.popleft()
                for li in ajl[c]:
                    if visited[li] == -1:
                        visited[li] = 1
                        q.append(li)

        #  outer loop
        components = 0
        for i in range(n):
            if visited[i] == -1:
                components +=1
                bfs(i)

        return components

        