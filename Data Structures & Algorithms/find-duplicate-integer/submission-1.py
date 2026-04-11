class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        self.duplicateNum = 0

        for i in range(1,len(nums)):
            if not nums[i-1] ^ nums[i]:
                self.duplicateNum = nums[i]
                break
        
        return self.duplicateNum