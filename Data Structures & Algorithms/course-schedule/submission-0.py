class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)] 
        for u,v in prerequisites:
            adjList[u].append(v)

        state = [0] * numCourses
        def dfs(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            state[node] = 1        
            for nextcourse in adjList[node]:
                    if dfs(nextcourse):
                        return True

            state[node] = 2

            return False

        for i in range(numCourses):
            if state[i] == 0:
                if dfs(i):
                    return False

        return True                           



        