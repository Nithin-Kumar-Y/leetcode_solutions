class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        a = len(s)
        b = len(t)
        dp = [[0]*(a+1) for _ in range(b+1)]
        for i in range(a+1):
            dp[0][i] = 1
        for i in range(1,b+1):
            for j in range(i, a+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]