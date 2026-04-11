class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        finalList = []

        def backtracking(open, close, slate):
            if (open + close) == 2*n:
                finalList.append("".join(slate))

            if open < n:
                slate.append("(")
                backtracking(open + 1 ,close , slate)
                slate.pop()
            if close < open:
                slate.append(")")
                backtracking(open ,close + 1 , slate)
                slate.pop() 

            return 
        
        backtracking(0,0,[])
        return finalList
