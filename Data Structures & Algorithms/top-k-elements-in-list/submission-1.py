class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a hashmap , with key and values as the number of repetitions
        # traverse a loop for k times
        #  inside there will be inner loop with find highest element each time.

        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1        

        minheap = []

        for key, count in hashMap.items():
            heapq.heappush(minheap, (count,key))
            if len(minheap) > k:
                heapq.heappop(minheap)


        return [num for count,num in minheap]        