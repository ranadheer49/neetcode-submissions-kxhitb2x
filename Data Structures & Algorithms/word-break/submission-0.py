class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        table = [0] * (n+1)
        table[0] = 1

        for i in range(1, n+1):
            for lstWrdLen in range(1, i+1):

                if s[i-lstWrdLen: i] in wordSet and table[i-lstWrdLen] == 1:
                    table[i] = 1

        return bool(table[-1])            
        