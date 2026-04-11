class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  list of number, each has a repetition
        #  return top repeated elements as per their repetion.
        repMap = {}
        finalList = []
        for num in nums:
            repMap[num] = repMap.get(num,0) + 1

        minHeap = []
        for num, reps in repMap.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap,(reps,num))
            else:
                topReps, tempNum = minHeap[0]
                if reps > topReps:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap,(reps,num))

        for i in range(0,k):
            _,key = heapq.heappop(minHeap)
            finalList.append(key)

        return finalList               
