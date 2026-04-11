class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1set = set()
        num2set = set()
        finalList = []
        for num in nums1:
            num1set.add(num)

        for num in nums2:
            num2set.add(num)

        for num in num1set:
            if num in num2set:
                  finalList.append(num)


        return finalList            