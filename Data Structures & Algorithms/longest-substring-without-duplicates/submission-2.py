class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        globalMax = [float("-inf")]
        parsedChars = set()

        lp,rp = 0,0
        if len(s) <= 0:
            return 0

        while rp < len(s):
            if s[rp] not in parsedChars: 
                parsedChars.add(s[rp])    
            else :
                while s[lp] != s[rp]:
                    parsedChars.remove(s[lp])
                    lp += 1
                lp += 1
            

            globalMax[0] = max(globalMax[0], rp - lp + 1)
            rp += 1

        return globalMax[0]    