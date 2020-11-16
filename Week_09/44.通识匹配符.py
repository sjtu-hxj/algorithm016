class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = '0' + s
        p = '0' + p
        # dp[i][j]表示：s的前i个字符与p的前j个字符是否匹配
        dp = [[False for _ in range(len(p))] for _ in range(len(s))]

        # 初始化
        dp[0][0] = True  # 空字符串与空字符串相匹配
        for i in range(1, len(p)):
            dp[0][i] = dp[0][i - 1] and p[i] == '*'
        for i in range(1, len(s)):
            dp[i][0] = False

        # 动态规划
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]