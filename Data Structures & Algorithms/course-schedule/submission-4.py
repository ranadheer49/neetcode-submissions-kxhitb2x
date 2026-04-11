class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #    Kahn's Algorithm
    #  create a adjList in reverse
    #  pick on with 0 indegree and put it in queue.
    #  at end compare completed with no of courses.
        inDegree = [0] * numCourses
        adjList = { i: [] for i in range(numCourses)}
        for course, preq in prerequisites:
            adjList[preq].append(course)
            inDegree[course] += 1

        que = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                que.append(i)

        visited = 0

        while que:
            cur = que.popleft()
            visited += 1

            for preq in adjList[cur]:
                inDegree[preq] -= 1
                if inDegree[preq] == 0:
                    que.append(preq)
        return visited == numCourses                        
