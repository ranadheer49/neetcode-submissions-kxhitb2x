class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        table = [0] * (len(cost)+1)

        table[1] = cost[0]
        for i in range(2,len(table)):
            table[i] = min(table[i-1],table[i-2]) + cost[i-1]

        return min(table[-1],table[-2])    
        