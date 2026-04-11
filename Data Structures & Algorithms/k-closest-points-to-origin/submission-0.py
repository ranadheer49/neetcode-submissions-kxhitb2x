class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        finalResult = []

        for x,y in points:
            dist = math.sqrt(pow(x,2) + pow(y,2))
            heapq.heappush(heap,(-dist,[x,y]))
            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            finalResult.append(heapq.heappop(heap)[1])
        return finalResult       
        