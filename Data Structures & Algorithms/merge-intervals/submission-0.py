class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        finalList = []

        i = 0
        while i < len(intervals):
            curStrtTime = intervals[i][0]
            curEndTime = intervals[i][1]
            while i+1 < len(intervals) and curEndTime >= intervals[i+1][0]:
                curEndTime = max(curEndTime,intervals[i+1][1] )
                i = i+1

            finalList.append([curStrtTime,curEndTime])
            i = i+1

        return finalList    
