class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #  to loop over set starting with first element, check if this is already visited
        #  if yes dont go inside
        #  else check the decrement values in a loop and then increment values in a loop
        #  increment the counter and also add to the visited set
        if not nums:
            return 0

        orgset = set(nums)
        visited = set()
        conslen = 0
        for val in orgset:
            if val in visited:
                continue
            temp = val
            templen = 1
            while temp-1 not in visited and temp -1 in orgset:
                    templen += 1
                    visited.add(temp-1)
                    temp = temp -1


            while  val + 1 not in visited and val +1 in orgset:
                       templen += 1  
                       visited.add(val+1)
                       val = val + 1

            if templen > conslen:
                conslen = templen


        return conslen                  


        