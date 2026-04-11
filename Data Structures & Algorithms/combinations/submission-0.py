class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        finalList = []

        def cHelper(n,k,i,slate):

            if len(slate) == k:
                finalList.append(slate[:])
                return
            
            if i > n:
                return

            slate.append(i)
            cHelper(n,k,i+1,slate)
            slate.pop()
            cHelper(n,k,i+1,slate)

        cHelper(n,k,1,[])
        return finalList    

        