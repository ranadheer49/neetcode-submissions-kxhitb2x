class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPlaindrome(start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1    
            return True        


        def helper(n):

            if n == 1:
                return s[0]

            for i in range(0, len(s)-n+1):

                if isPlaindrome(i,n+i-1):
                    return s[i:n+i]
                # else :
                #     helper(n-1)
            return helper(n-1)

        return helper(len(s))



