class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rIndex = 0
        bIndex = len(nums) - 1
        travIndex = 0

        while travIndex <= bIndex :

            if nums[travIndex]  == 0:
                nums[rIndex],nums[travIndex] = nums[travIndex] , nums[rIndex]
                rIndex += 1
                travIndex += 1
            elif nums[travIndex] == 2:
                 nums[bIndex],nums[travIndex] = nums[travIndex] , nums[bIndex]
                 bIndex -= 1    
            else:
                travIndex += 1
      