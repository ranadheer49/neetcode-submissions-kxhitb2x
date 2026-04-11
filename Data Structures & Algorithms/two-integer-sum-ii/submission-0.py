class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#  use 2 pointer approach to find the sum
#  left index 0 right index len - 1
#  if sum is less than target increase the left index
#  if sum is greated than target decrease the right index
#  if sum is equal to targe then return the indices

        leftIndex = 0
        rightIndex = len(numbers) - 1

        while leftIndex < rightIndex:
            sum = numbers[leftIndex]  + numbers[rightIndex]
            if sum < target:
                leftIndex += 1
            elif  sum > target:
                rightIndex -= 1
            else :
                return [leftIndex + 1 ,rightIndex + 1]    



