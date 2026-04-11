class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.finalList = []    
        i = 0




        def helper(nums, i, slate):

            if i >= len(nums):
                self.finalList.append(slate[:])
                return
            slate.append(nums[i])
            helper(nums, i+1, slate)
            slate.pop()
            helper(nums, i+1, slate)

        tempList = []
        helper(nums, i , tempList)


        return self.finalList     
        