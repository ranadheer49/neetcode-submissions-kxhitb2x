class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        mergedList = []
        for start, end in intervals:
            if not mergedList or mergedList[-1][1] < start:
                mergedList.append([start,end])
            else:
                if mergedList[-1][1] < end:
                    mergedList[-1][1] = end

        return mergedList            



