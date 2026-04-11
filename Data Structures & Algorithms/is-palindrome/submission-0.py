class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        leftindex = 0
        rightindex = len(s)-1

        while leftindex < rightindex:
            while not self.isAlphaNumeric(s[leftindex]) and leftindex < rightindex:
                leftindex += 1

            while not self.isAlphaNumeric(s[rightindex]) and leftindex < rightindex:
                rightindex -= 1

            if s[leftindex].lower() == s[rightindex].lower():
                leftindex += 1
                rightindex -= 1
            else : 
                return False    

        return True        

    def isAlphaNumeric(self, c) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z') or 
                ord('0') <= ord(c) <= ord('9'))   