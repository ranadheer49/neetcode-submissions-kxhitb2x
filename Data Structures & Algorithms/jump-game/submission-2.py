class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def helper(pos):
            if pos in memo:
                return memo[pos]

            if pos == len(nums) -1 :
                return True

            if nums[pos] == 0:
                return False

            for i in range(1,nums[pos]+1):

               if helper(pos+i):
                  memo[pos] = True
                  return True
            memo[pos] = False
            return False
        return helper(0)          


        