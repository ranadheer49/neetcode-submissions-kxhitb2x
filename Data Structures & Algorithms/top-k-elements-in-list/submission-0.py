class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a hashmap , with key and values as the number of repetitions
        # traverse a loop for k times
        #  inside there will be inner loop with find highest element each time.

        repMap = defaultdict(int)
        output = []
        for num in nums:
            repMap[num] += 1

        for i in range(k):
            highcount = 0
            highkey = None
            for key, value in repMap.items():
                if value >= highcount and key not in output:
                    highcount = value
                    highkey = key
            
            output.append(highkey) 

        return output           