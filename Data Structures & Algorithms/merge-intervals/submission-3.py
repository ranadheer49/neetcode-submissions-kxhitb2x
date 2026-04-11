class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        mergedList = []
        for start, end in intervals:
            if not mergedList or mergedList[-1][1] < start:
                mergedList.append([start,end])
            else:
                
                mergedList[-1][1] = max(mergedList[-1][1], end)

        return mergedList            



