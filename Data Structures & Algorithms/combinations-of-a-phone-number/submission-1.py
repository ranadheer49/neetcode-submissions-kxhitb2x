class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        finalList = []
        if not digits:
            return []
        numMap = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz' 
        }

        def lcHelper(i,slate):
            if i == len(digits):
                finalList.append(''.join(slate))
                return
            tempStr = numMap.get(digits[i])
            for j in range(0,len(tempStr)):
                slate.append(tempStr[j])
                lcHelper(i+1,slate)
                slate.pop()


        lcHelper(0,[])
        return finalList          