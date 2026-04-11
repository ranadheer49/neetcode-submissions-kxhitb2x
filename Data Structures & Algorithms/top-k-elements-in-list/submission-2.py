class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] = map.get(num,0) + 1
        heap = []

        for key,value in map.items():
            heapq.heappush(heap,(-value,key)) 

        finalList = []
        for i in range(0,k):
            _,key = heapq.heappop(heap)
            finalList.append(key)

        return finalList