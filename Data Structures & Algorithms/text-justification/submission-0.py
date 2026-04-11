class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        length = 0
        i =0

        while i< len(words):
            if length + len(line) + len(words[i]) <= maxWidth:
                length += len(words[i])
                line.append(words[i])
                i += 1
            else:
                spaceLen = maxWidth - length
                reminder = spaceLen % max(1,(len(line)-1))
                addSpace = spaceLen // max(1,(len(line) -1))
                
                for j in range(max(1,len(line)-1)):
                    line[j] += " " * addSpace
                    if reminder > 0:
                        line[j] += " "
                        reminder -= 1

                res.append("".join(line))
                line, length = [],0

    #  last line 
        last_line = " ".join(line)
        trial_spaces = maxWidth - len(last_line)
        res.append(last_line + " "*trial_spaces)
        return res


                     

