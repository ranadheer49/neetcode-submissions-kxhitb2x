class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        finalList = []
        candidates.sort()

        def csHelper(i,sum,slate):

            if sum == target:
                finalList.append(slate[:])
                return
            if sum > target or i == len(candidates):
                return


            
            slate.append(candidates[i])
            csHelper(i+1,sum + candidates[i],slate)
            slate.pop()

            
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            csHelper(i+1,sum,slate)


        csHelper(0,0,[])
        return finalList    
            

        