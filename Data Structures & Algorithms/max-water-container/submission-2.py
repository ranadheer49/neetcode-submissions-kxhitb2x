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
            # update the global max every time.
            maxWater = max(maxWater, min(heights[left], heights[right]) * (right - left))

            # decrement right pointer if left bar height is more than the right bar.
            if heights[left] > heights[right]:
                right -= 1
            # increment left pointer if right bar height is more than the left bar 
            else:
                left += 1

        return maxWater            

        