""" DP30: 买卖股票的最好时机(一) """

# 题目要求：
# 假设你有一个数组prices，长度为n，其中prices[i]是股票在第i天的价格，
# 请根据这个价格数组，返回买卖股票能获得的最大收益
# 1.你可以买入一次股票和卖出一次股票，并非每天都可以买入或卖出一次，
#   总共只能买入和卖出一次，且买入必须在卖出的前面的某一天
# 2.如果不能获取到任何利润，请返回0
# 3.假设买入卖出均无手续费

n = 7
prices = [8, 9, 2, 5, 4, 7, 1]

# 连续最大子数组和
# d_vals = [vals[i+1] - vals[i] for i in range(len(vals)-1)]
dp = [float("-inf") for _ in range(len(prices))]

for i in range(1, len(prices)):
    # dp[i] = max(d_vals[i-1], dp[i-1] + d_vals[i-1])
    dp[i] = max(
        prices[i] - prices[i-1],
        dp[i-1] + prices[i] - prices[i-1]
    )

if max(dp) < 0:
    print(0)
else:
    print(max(dp))
