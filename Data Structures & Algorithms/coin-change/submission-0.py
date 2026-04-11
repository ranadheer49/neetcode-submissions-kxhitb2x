class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        table = [math.inf] * (amount + 1)

        table[0] = 0

        for i in range(1,len(table)):

            for c in coins:

                if i -c >= 0:
                    table[i] = min(table[i-c],table[i])
            table[i] += 1
        if table[-1] != math.inf:
            return table[-1]

        return -1                
        