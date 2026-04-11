class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        finalList = []

        def permHelper(nums,i,slate):

            if i == len(nums):
                finalList.append(slate[:])
                return

            for j in range(i,len(nums)):

                nums[i], nums[j] = nums[j], nums[i]
                slate.append(nums[i])
                permHelper(nums, i+1, slate )
                slate.pop()
                nums[i], nums[j] = nums[j], nums[i]




        permHelper(nums, 0 , [])
        
        return finalList