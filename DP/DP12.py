""" DP12: 龙与地下城游戏问题 """

# 题目要求：
# 给定一个二维数组map，含义是一张地图。
# 游戏的规则如下:
# 1）骑士从左上角出发，每次只能向右或向下走，最后到达右下角见到公主。
# 2）地图中每个位置的值代表骑士要遭遇的事情。如果是负数，说明此处有怪兽，要让骑士损失血量。如果是非负数，代表此处有血瓶，能让骑士回血。
# 3）骑士从左上角到右下角的过程中，走到任何一个位置时，血量都不能少于1。为了保证骑土能见到公主，初始血量至少是多少?
# 根据map, 输出初始血量。

# 备注：
# 时间复杂度：O(n∗m)
# 额外空间复杂度：O(min(n,m))

n, m = 3, 3
_map = [
    [-2, -3, 3],
    [-5, -10, 1],
    [0, 30, -5]
]

dp = [0 for _ in range(m)]
if m > n:  # 使得时间复杂度最小
    _map = list(map(lambda x: list(x), list(zip(*_map))))  # 转置
tmp = n
m = n
n = tmp

event = None
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if _map[i][j] > 0:
            event = "血瓶"
        elif _map[i][j] == 0:
            event = "空房间"
        else:
            event = "怪物"
        # print(f"第{i+1}行，第{j+1}列，勇者遇到了{event}")

        if i != n-1 and j != m-1:
            dp[j] = max(min(dp[j+1], dp[j]) - _map[i][j], 1)
        elif i == n-1 and j != m-1:
            dp[j] = max(dp[j+1] - _map[i][j], 1)
        elif i != n-1 and j == m-1:
            dp[j] = max(dp[j] - _map[i][j], 1)
        else:
            dp[j] = max(1 - _map[i][j], 1)  # 最后一格血量

print(dp[0])
