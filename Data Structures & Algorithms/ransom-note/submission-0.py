class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        inputMap = defaultdict(int)

        for c in magazine:
            inputMap[c] += 1

        for c in ransomNote:
            if inputMap[c] < 1:
                return False

            inputMap[c] -= 1

        return True               
