class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    #    words = ["This","is","an","example","of","text","justification."], maxWidth = 16
    # Output: [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
        # ]
        finalRes = []
        length = 0
        line = []
        i = 0

        while i < len(words):
            if length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                length += len(words[i])
                i += 1
            else:

                remSpace = maxWidth - length
                space = remSpace // max(1,len(line)-1)
                leftOverSpaces =  remSpace % max(1,len(line)-1)

                for j in range(max(1,len(line) -1)):
                    line[j] += " " * space
                    if leftOverSpaces:
                        line[j] += " "
                        leftOverSpaces -= 1
                finalRes.append("".join(line))
                length = 0
                line = []

        finalline = " ".join(line)
        finalline = finalline + " " * (maxWidth - len(finalline))
        finalRes.append(finalline)
        return  finalRes       

