
array = [
    ["aab"],  # str
    ["c*a*b"]  # pattern
]

# 匹配任意字符串
if array[1][0] == ".*":
    print("true")
    exit(0)

# 手动分隔
_str = list(array[0][0])
pattern = list(array[1][0])
tmp = [pattern[i] + pattern[i + 1] for i in range(len(pattern) - 1)]
for i in range(len(pattern) - 1):
    if tmp[i][1] == "*":
        pattern[i] = tmp[i]
pattern = list(filter(lambda x: x != "*", pattern))
print(_str, pattern)
# 动态规划数组
# dp[i][j]表示str前i个字符能否被pattern前j个字符匹配
dp = [
    ["false" for _ in range(len(pattern) + 1)] for _ in range(len(_str) + 1)
]
for i in range(len(pattern) + 1):
    dp[0][i] = "true"

# 转移条件为：
# (1) dp[i-1][j-1]或dp[i-1][j]匹配
# (2) _str[i]与pattern[j]匹配
# (3) 对于a和a*而言，转移式不同
for i in range(1, len(_str) + 1):
    for j in range(1, len(pattern) + 1):
        char, match = _str[i - 1], pattern[j - 1]
        if match == "." or match == char:  # .或a-z
            if dp[i - 1][j - 1] == "true":
                dp[i][j] = "true"
        elif match[0] == char:  # 任意个a-z
            if dp[i - 1][j - 1] == "true" or dp[i - 1][j] == "true":
                dp[i][j] = "true"

print(dp)

# TODO: 待求解