class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp=[0]*(col+1)
        dp[1]=1
        for j in range(2, col+1):
            if obstacleGrid[0][j-1]==1:
                dp[j]=0
            else:
                dp[j]=dp[j-1]
        for i in range(1, row):
            for j in range(1, col+1):
                if obstacleGrid[i][j-1]==1:
                    dp[j]=0
                else:
                    dp[j]+=dp[j-1]
        return dp[col]