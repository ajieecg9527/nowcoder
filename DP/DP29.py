""" DP29: 过河 """

# 题目要求
# 在河上有一座独木桥，一只青蛙想沿着独木桥从河的一侧跳到另一侧。
# 在桥上有一些石子，青蛙很讨厌踩在这些石子上。
# 由于桥的长度和青蛙一次跳过的距离都是正整数，
# 我们可以把独木桥上青蛙可能到达的点看成数轴上的一串整点：
# 0，1，……，L（其中L是桥的长度）。
# 坐标为0的点表示桥的起点，坐标为L的点表示桥的终点。
# 青蛙从桥的起点开始，不停的向终点方向跳跃。
# 一次跳跃的距离是S到T之间的任意正整数（包括S,T）。
# 当青蛙跳到或跳过坐标为L的点时，就算青蛙已经跳出了独木桥。
# 题目给出独木桥的长度L，青蛙跳跃的距离范围S,T，桥上石子的位置。
# 你的任务是确定青蛙要想过河，最少需要踩到的石子数。

L = 10  # 桥的长度
S, T, M = 2, 3, 5  # 跳跃最小/大距离，桥上石子个数
stone_indexes = [2, 3, 5, 6, 7]  # 石子

# 对Python而言，这道题的难点在于如何对于S-T降维
dp = [float("-inf") for _ in range(L+T)]  # 一些格子不能到达
stones = [0 for _ in range(L+T)]
for index in stone_indexes: # 初始化石子下标
    stones[index] = 1
for i in range(S, T+1):  # 初始化dp数组（在范围S-T）
    if stones[i] == 1:
        dp[i] = 1
    else:
        dp[i] = 0
dp[0] = 0  # 桥的终点算跳的最小步

# dp[i]表示第i个整点
for i in range(T+1, L+T):
    choices = []
    for j in range(S, T+1):
        if dp[i-j] >= 0:
            choices.append(dp[i-j]+stones[i])
    if len(choices) != 0:
        dp[i] = min(choices)

results = list(filter(lambda x: x >= 0, dp[L:]))
print(min(results))
