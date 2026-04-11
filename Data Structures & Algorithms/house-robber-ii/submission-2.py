class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]  
                        
            table = [0] * (len(nums) + 1)
            table[1] = nums[0]

            for i in range(2, len(nums) +1):

                table[i] = max(table[i-1] , table[i-2] + nums[i-1])

            return table[-1]  

        return max(helper(nums[1:]) , helper(nums[:-1]))     
        