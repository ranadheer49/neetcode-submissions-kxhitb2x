class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charMap = [0] * 26
        finalRes = 0

        for c in chars:
            charMap[ord(c) - ord('a')] += 1

        for word in words:
            isValid = True
            wordMap = [0] * 26
            for c in word:
                wordMap[ord(c) - ord('a')] += 1
                if  wordMap[ord(c) - ord('a')] >  charMap[ord(c) - ord('a')]:
                      isValid = False
                      break

            if isValid:
                finalRes += len(word)           

        return finalRes    

        