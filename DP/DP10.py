""" DP10: 最大子矩阵 """

# 题目要求：
# 已知矩阵的大小定义为矩阵中所有元素的和。给定一个矩阵，
# 你的任务是找到最大的非空(大小至少是1 * 1)子矩阵。
# 比如，如下4 * 4的矩阵
# 0 -2 -7 0 9 2 -6 2 -4 1 -4 1 -1 8 0 -2
# 的最大子矩阵是 9 2 -4 1 -1 8
# 这个子矩阵的大小是15。

n = 4
matrix = [
    [0, -2, -7, 0],
    [9, 2, -6, 2],
    [-4, 1, -4, 1],
    [-1, 8, 0, -2]
]

# 行前缀相加
row_sums = [[sum(matrix[i][:j+1]) for j in range(n)] for i in range(n)]

def cslms(ns: list):
    res, temp_max = ns[0], ns[0]
    for n in ns[1:]:
        temp_max = n + temp_max if temp_max > 0 else n
        res = temp_max if res < temp_max else res
    return res

max_sum = row_sums[0][0]
for j in range(n):
    for i in range(j):
        # lin[k] 是输入矩阵第k行第i+2个数加到第j+1个数，i<j
        lin = [row_sums[k][j] - row_sums[k][i] for k in range(n)]
        maxi = max(max_sum, cslms(lin))
    # 补充 i=j 的情况
    lin = [row_sums[k][j] for k in range(n)]
    maxi = max(max_sum, cslms(lin))
print(max_sum)

# TODO: 写代码注释