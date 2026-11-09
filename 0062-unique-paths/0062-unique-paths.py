class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp= [1]*(n+1)
        dp[0]=0
        for i in range(m-1):
            for j in range(1, n+1):
                dp[j]= dp[j]+dp[j-1]
        return dp[n]