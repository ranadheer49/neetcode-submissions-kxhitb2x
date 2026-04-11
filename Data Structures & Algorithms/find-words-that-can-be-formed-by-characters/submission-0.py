class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freqMap = {}
        totalLen = [0]
        for c in chars:
            freqMap[c] = freqMap.get(c,0) + 1
        def wordExists(word):
            charMap = {}
            for c in word:
                charMap[c] = charMap.get(c,0) + 1
                if c not in freqMap or charMap[c] > freqMap[c]:
                    return False
            return True
            
        for word in words:
            if wordExists(word):
                totalLen[0] = totalLen[0] + len(word)

        return totalLen[0]        



        