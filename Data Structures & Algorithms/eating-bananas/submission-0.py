class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#  [1,4,3,2], h = 9
#  min = 1
#  brute force is trying from 1 to max of piles. O(k * K)
#  can make this better doing binary search  O(k * log K)

        l , r  = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r)//2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(float(piles[i])/k)

            if hours <= h:
                res = min(k ,res)
                r = k-1
            else:
                l = k+1

        return res                



        