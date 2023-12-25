""" DP31: 买卖股票的最好时机(二) """

# 题目要求：
# 假设你有一个数组prices，长度为n，其中prices[i]是股票在第i天的价格，
# 请根据这个价格数组，返回买卖股票能获得的最大收益
# 1.你可以多次买卖该只股票，但是再次购买前必须卖出之前的股票
# 2.如果不能获取到任何利润，请返回0
# 3.假设买入卖出均无手续费

n = 7
prices = [8, 9, 2, 5, 4, 7, 1]

# 求所有正数差值之和
pos_sum = 0
for i in range(len(prices)-1):
    if prices[i+1] - prices[i] > 0:
        pos_sum += prices[i+1] - prices[i]
print(pos_sum)
