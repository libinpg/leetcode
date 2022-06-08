from cmath import inf

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        p1 = 0
        p2 = len(prices) - 1
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit
#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
with open(r'prices1.txt', 'r') as f:
    lines = f.readlines()
readStr = ""
for l in lines:
    readStr += l.rstrip('\n')
prices = readStr.split(',')
for i in range(len(prices)):
    prices[i] = int(prices[i])
#prices = [7,6,4,3,1]
#prices = [2,1]
#prices = [3,3]
#prices = [2,4,1]
print(Solution().maxProfit(prices))