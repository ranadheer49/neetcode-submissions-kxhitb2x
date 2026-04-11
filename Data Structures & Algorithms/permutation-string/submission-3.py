class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       if len(s2) < len(s1):
        return False
       s1OrdList = [0] * 26      
       s1len = len(s1)

       for c in s1:
        s1OrdList[ord(c) - ord('a')] += 1

       def strEquality(input):
        s2OrdList = [0] * 26
        for c in input:            
            s2OrdList[ord(c) - ord('a')] += 1
        return s2OrdList == s1OrdList

       for i in range(0,len(s2) - len(s1) + 1):
        if s2[i] in s1:
            if strEquality(s2[i:i+len(s1)]):
                return True
       return False         

        

        
