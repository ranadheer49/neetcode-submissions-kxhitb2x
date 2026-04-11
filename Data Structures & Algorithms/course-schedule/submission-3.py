class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        status =[0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, preq in prerequisites:
            adj[course].append(preq)

        def dfs(course):
            if status[course] == 1:
                return True
            if status[course] == 2:
                return False
            status[course] = 1
            for preq in adj[course]:
                
                if dfs(preq):
                    return True
                  
            status[course] = 2
            return False


        for course in adj:
            for preq in course:
                if status[preq] == 0:
                    if dfs(preq):
                        return False
        return True            


     