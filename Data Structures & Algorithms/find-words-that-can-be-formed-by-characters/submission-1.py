class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charMap = defaultdict(int)
        finalRes = 0

        for c in chars:
            charMap[c] =  charMap.get(c,0) + 1

        for word in words:
            wordMap = defaultdict(int)
            isValid = True
            for c in word:
                wordMap[c] += 1
                if wordMap[c] > charMap[c]:
                    isValid = False
                    break
            if isValid:
                finalRes += len(word)        

        return finalRes    

        