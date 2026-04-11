class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        finalList = []

        def puHelper(i,slate):

            if i == len(nums):
                finalList.append(slate[:])
                return


            tempSet = set()

            for j in range(i,len(nums)):
                nums[i],nums[j] = nums[j],nums[i] 
                if nums[i] not in tempSet:
                    
                    tempSet.add(nums[i])
                    slate.append(nums[i])
                    puHelper(i+1,slate)
                    slate.pop()   
                nums[i],nums[j] = nums[j],nums[i] 


        puHelper(0,[])
        return finalList    