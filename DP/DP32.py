""" DP32: 买卖股票的最好时机(三) """

# 题目要求：
# 假设你有一个数组prices，长度为n，其中prices[i]是股票在第i天的价格，
# 请根据这个价格数组，返回买卖股票能获得的最大收益
# 1.你最多可以对该股票有两笔交易操作，
# 一笔交易代表着一次买入与一次卖出，但是再次购买前必须卖出之前的股票
# 2.如果不能获取到任何利润，请返回0
# 3.假设买入卖出均无手续费

n = 6
prices = [8, 9, 3, 5, 1, 3]

# 1. 空间复杂度O(n), 时间复杂度O(n)
# 2. 优化空间：空间复杂度O(1)
# dp = [[0 for _ in range(5)] for _ in range(len(prices))]
dp = [0 for _ in range(5)]
# dp[0][0], dp[0][2], dp[0][4] = 0, 0, 0
# dp[0][1], dp[0][3] = -prices[0], -prices[0]
dp[0], dp[2], dp[4] = 0, 0, 0
dp[1], dp[3] = -prices[0], -prices[0]

for i in range(1, len(prices)):
    # dp[i][0] = dp[i-1][0]
    # dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
    dp[1] = max(dp[1], dp[0] - prices[i])
    # dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
    dp[2] = max(dp[2], dp[1] + prices[i])
    # dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
    dp[3] = max(dp[3], dp[2] - prices[i])
    # dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
    dp[4] = max(dp[4], dp[3] + prices[i])

# print(dp[-1][-1])
print(dp[-1])
