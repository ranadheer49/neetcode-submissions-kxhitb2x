class Solution:
    def isHappy(self, n: int) -> bool:
        visitedNumbers = set()

        while n not in visitedNumbers:
            visitedNumbers.add(n)
            tempSum = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                tempSum = tempSum + digit
                n = n //10
   
            n = tempSum
            
            if n == 1:
                return True  
        return False          




        