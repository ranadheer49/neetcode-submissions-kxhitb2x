"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# [(0,40),(5,10),(15,20)]   
#  2
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        maxRooms = 0
        startTimes , endTimes= [] , []
        for i in range(len(intervals)):
            startTimes.append(intervals[i].start)
            endTimes.append(intervals[i].end)
        startTimes.sort()
        endTimes.sort()

        ps, pe = 0 , 0

        for j in range(len(endTimes)):

            while ps < len(startTimes) and endTimes[j] > startTimes[ps]:
                count += 1
                ps += 1
                maxRooms = max(maxRooms, count)
            count -= 1  

        return maxRooms      


        