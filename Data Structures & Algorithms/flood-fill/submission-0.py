class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        def neighbours(r,c):
            n = []
            if r+1 < len(image):
                n.append((r+1,c))
            if c+1 < len(image[0]):
                n.append((r,c+1))
            if r-1 >= 0:
                n.append((r-1,c))
            if c-1 >=0:
                n.append((r,c-1))  
            return n

        def bfs(sr,sc,color):
            if image[sr][sc] == color:
                return image
            ecolor = image[sr][sc]
            q = deque()
            q.append((sr,sc))
            image[sr][sc] = color
            while q:
                r,c = q.popleft()

                for nr,nc in neighbours(r,c):

                    if image[nr][nc] == ecolor:
                        image[nr][nc] = color
                        q.append((nr,nc))

        bfs(sr,sc,color)
        return image                
