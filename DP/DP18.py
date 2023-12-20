""" DP18: 滑雪 """

# 题目要求
# 给定一个n*m的矩阵，矩阵中的数字表示滑雪场各个区域的高度。
# 你可以选择从任意一个区域出发，并滑向任意一个周边的高度严格更低的区域（周边的定义是上下左右相邻的区域）。
# 请问整个滑雪场中最长的滑道有多长？(滑道的定义是从一个点出发的一条高度递减的路线）。
# (本题和矩阵最长递增路径类似，该题是当年NOIP的一道经典题)

import itertools

n, m = 4, 5
ski_slope = [
    [45, 15, 38, 34, 35],
    [3, 7, 39, 39, 49],
    [32, 29, 5, 27, 48],
    [16, 47, 24, 16, 36]
]

# 动态规划数组和结构数组
dp = [[1 for _ in range(m)] for _ in range(n)]
coords = [(ski_slope[i][j], (i, j)) for i in range(n) for j in range(m)]
coords.sort(key=lambda x: x[0], reverse=True)

while len(coords) != 0:
    h, c = coords.pop(0)  # 高度，坐标
    i, j = c  # 坐标

    choices = []
    if i != 0 and h < ski_slope[i-1][j]:
        choices.append(dp[i-1][j] + 1)  # 向上滑
    if i != n - 1 and h < ski_slope[i+1][j]:
        choices.append(dp[i+1][j] + 1)  # 向下滑
    if j != 0 and h < ski_slope[i][j-1]:
        choices.append(dp[i][j-1] + 1)  # 向左滑
    if j != m - 1 and h < ski_slope[i][j+1]:
        choices.append(dp[i][j+1] + 1)  # 向右滑
    dp[i][j] = max(choices + [1])

dp = list(itertools.chain(*dp))  # 二维列表扁平化处理
print(max(dp))