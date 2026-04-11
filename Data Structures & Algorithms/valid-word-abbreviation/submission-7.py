class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wstart , astart = 0, 0
        wend, aend = len(word), len(abbr)
        while wstart < wend and astart < aend:
            digit = 0
            if abbr[astart] == '0':
                return False

            if word[wstart] == abbr[astart]:
                wstart += 1
                astart += 1 
            elif abbr[astart].isalpha():
                return False
            else:    
                while astart < aend and abbr[astart].isnumeric():
                    digit = (digit * 10) + int(abbr[astart])
                    astart += 1
                wstart += digit
            

        return wstart == wend and astart == aend       
        