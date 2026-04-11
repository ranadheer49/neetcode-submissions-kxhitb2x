class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedSet = set()
        start, end = 0, 0
        maxLength = 0 

        while end < len(s):
            if s[end] not in visitedSet:
                visitedSet.add(s[end])
                maxLength = max(maxLength , end-start+1)

            else:
                while s[start] != s[end]:
                    visitedSet.remove(s[start])
                    start += 1

                start += 1
            end += 1

        return maxLength        


        