class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        finalList = []

        def puHelper(nums,i,slate):

            if i == len(nums):
                finalList.append(slate[:])
                return


            tempSet = set()

            for j in range(i,len(nums)):
                
                if nums[j] not in tempSet:
                    nums[i],nums[j] = nums[j],nums[i]
                    tempSet.add(nums[i])
                    slate.append(nums[i])
                    puHelper(nums,i+1,slate)
                    slate.pop()   
                    nums[i],nums[j] = nums[j],nums[i] 


        puHelper(nums,0,[])
        return finalList    