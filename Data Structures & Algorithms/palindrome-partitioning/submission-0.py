class Solution:
    def partition(self, s: str) -> List[List[str]]:

        self.finalList = []


        def helper(s,start,partitions):

            if start == len(s):
                self.finalList.append(partitions[:])


            for j in range(start,len(s)):
                if ispalindrome(self,s,start,j):
                    partitions.append(s[start:j+1])
                    helper(s,j+1,partitions)
                    partitions.pop()


        def ispalindrome(self,s,i,j) -> bool:
          
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1
            return True

        helper(s,0,[])

        return self.finalList                
        