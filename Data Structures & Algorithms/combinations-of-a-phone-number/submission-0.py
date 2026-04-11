class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.numMap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        self.finalList = []
 

        
        def findComb(digits, start, slate):

            if start >= len(digits):
                self.finalList.append("".join(slate))
                return 

            num = digits[start]
            chars = self.numMap[num]
            for i in range(0, len(chars)):
                slate.append(chars[i])
                findComb(digits, start+1 ,slate) 
                slate.pop() 

        findComb(digits,0,[])
        return self.finalList         

        
