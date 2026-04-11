class Solution:
    def rob(self, nums: List[int]) -> int:

        table = [0] * (len(nums) + 1)

        table[1] = nums[0]

        for i in range(2,len(nums)+1):

            table[i] = max(table[i-1], table[i-2]+ nums[i-1]) 

        return max(table[-1], table[-2])    
        