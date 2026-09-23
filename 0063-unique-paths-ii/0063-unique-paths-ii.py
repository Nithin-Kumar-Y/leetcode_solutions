class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        m = len(obstacleGrid[0])  # columns
        n = len(obstacleGrid)  # rows
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        dp[1][1]=1
        # base case
        for i in range(2, m+1):
            if obstacleGrid[0][i-1] == 1:
                dp[1][i] = 0
            else:
                dp[1][i]=dp[1][i-1]
        for i in range(2, n+1):
            if obstacleGrid[i-1][0] == 1:
                dp[i][1] = 0
            else:
                dp[i][1]= dp[i-1][1]
        
        # transition state
        for i in range(2, n+1):
            for j in range(2, m+1):
                if obstacleGrid[i-1][j-1] != 1:
                    dp[i][j]= dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[n][m]