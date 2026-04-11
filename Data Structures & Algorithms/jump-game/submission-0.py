class Solution:
    def canJump(self, nums: List[int]) -> bool:


        def helper(pos):

            if pos == len(nums) -1 :
                return True

            if nums[pos] == 0:
                return False

            for i in range(1,nums[pos]+1):

               if helper(pos+i):
                  return True
            return False
        return helper(0)          


        