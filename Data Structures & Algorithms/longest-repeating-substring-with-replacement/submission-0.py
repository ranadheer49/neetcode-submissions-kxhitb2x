class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visitedChars = {}
        maxLen, maxFreq = 0,0
        li  = 0
        for ri in range(len(s)):
            visitedChars[s[ri]] = visitedChars.get(s[ri],0)+ 1
            maxFreq = max(maxFreq, visitedChars[s[ri]])

            while (ri - li +1) - maxFreq > k:
                visitedChars[s[li]] -=  1               
                if visitedChars[s[li]] == 0:
                    del visitedChars[s[li]]  
                li +=1     

            maxLen = max(maxLen , ri - li + 1)     

        return maxLen         


        