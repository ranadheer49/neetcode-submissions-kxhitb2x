class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def dfs(start,end):
            if start > end:
                return -1
            mid = (start + end)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return dfs(start, mid -1 )
            else:    
                return dfs(mid+1,end)  

        return dfs(0,len(nums)-1)          

        