class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        #  create a frequency MAP
        #  put them in the max heap
        #  while reducing the freq count put them in the queue
        freqMap = defaultdict(int)
        maxHeap = []
        q = deque()
        for task in tasks:
            freqMap[task] += 1          
                                        
        for task,value in freqMap.items():
            heapq.heappush(maxHeap,-value)
        time = 0
        while maxHeap or q:          
            if q and q[0][1] < time:
                heapq.heappush(maxHeap, -q.popleft()[0])
            if maxHeap:
                val = -heapq.heappop(maxHeap)
                if val > 1:
                    q.append((val-1,time + n))                    
            
            time += 1
        return time        





        