class Solution:
    def climbStairs(self, n: int) -> int:
        slate = [0] * 3
        slate[1] = 1
        slate[2] = 2
        if n == 1 or n == 2 :
            return n

        for i in range(3,n+1):
            slate[i%3] = slate[(i-1)%3] + slate[(i-2)%3]

        return slate[n%3]  

   


        