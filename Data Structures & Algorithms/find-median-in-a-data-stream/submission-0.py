class MedianFinder:

    def __init__(self):
        self.lHeap = []
        self.sHeap = []
        

    def addNum(self, num: int) -> None:
        if self.lHeap and num > self.lHeap[0]:
            heapq.heappush(self.lHeap, num)
        else:
            heapq.heappush(self.sHeap, -1*num)

        if len(self.sHeap) > len(self.lHeap) + 1:
            val = -1 * heapq.heappop(self.sHeap)
            heapq.heappush(self.lHeap, val)
        if len(self.lHeap) > len(self.sHeap) + 1:
            val = heapq.heappop(self.lHeap)
            heapq.heappush(self.sHeap, -1 * val)   


    def findMedian(self) -> float:
        if len(self.sHeap) > len(self.lHeap):
            return -1 * self.sHeap[0]
        elif len(self.lHeap) > len(self.sHeap):
            return self.lHeap[0]
        else:
            return (-1 * self.sHeap[0] + self.lHeap[0]) / 2.0        
        
        