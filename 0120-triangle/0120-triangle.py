class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        dp=triangle[0]
        for i in range(1, n):
            temp=[]
            for j in range(i+1):
                if j==0:
                    val=dp[0]+triangle[i][0]
                elif j==i:
                    val = dp[j-1]+triangle[i][i]
                else:
                    val = min(dp[j], dp[j-1])+triangle[i][j]
                temp.append(val)
            dp=temp
        return min(dp)