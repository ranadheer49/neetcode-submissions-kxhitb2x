class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       if len(s2) < len(s1):
        return False
       s1OrdList = [0] * 26  
       s2OrdList = [0] * 26    
       s1len = len(s1)

       for c in s1:
        s1OrdList[ord(c) - ord('a')] += 1
        
       left  = 0 
       for right in range(len(s2)):
        s2OrdList[ord(s2[right]) - ord('a')] += 1
        if right - left +1 > len(s1):
            s2OrdList[ord(s2[left]) - ord('a')] -= 1
            left += 1

        if s2OrdList == s1OrdList:
            return True    

       return False         

        

        
