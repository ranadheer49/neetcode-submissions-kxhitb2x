class Solution:
    def maxArea(self, heights: List[int]) -> int:
          #  initialise left and right pointer
        left = 0
        right = len(heights) - 1
      

        #  initialize maxWater to 0 initially
        maxWater = 0

        # loop until both pointers meet
        while left < right:
            #  each iteration, amount of water is equal to height of small bar * distance between bars
            maxWater = max(maxWater, min(heights[left], heights[right]) * (right - left))

            # increment left pointer if its height is more than the right pointer
            #  reason: 
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxWater            

        