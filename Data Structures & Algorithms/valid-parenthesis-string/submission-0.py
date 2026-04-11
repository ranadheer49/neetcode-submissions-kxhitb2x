class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        wild = []

        for i,c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                wild.append(i) 
            else: 
                if not left and not wild:
                    return False   
                if left:
                    left.pop()
                else:
                    wild.pop()

        while left and wild:
            if left.pop() > wild.pop():
                return False

        return not left                    
                 
        