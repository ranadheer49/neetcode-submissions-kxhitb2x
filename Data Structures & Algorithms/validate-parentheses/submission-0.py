class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingMap = {')' : '(',
                       '}' : '{',
                       ']' : '['}

        for i in range(len(s)):

            if s[i] in closingMap:
                if not stack:
                    return False
                elif stack[-1] != closingMap[s[i]]:
                    return False
                else:
                    stack.pop()      

            else: 
                stack.append(s[i])  

        if stack:
            return False
        return True                  

            

        