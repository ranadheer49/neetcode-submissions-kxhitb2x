class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = defaultdict(list)

        for iStr in strs:
            count = [0]*26
            for c in iStr:
                count[ord(c) - ord('a')] += 1
            strMap[tuple(count)].append(iStr)    

        return list(strMap.values())         