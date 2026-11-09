class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp= [0]*(n+1)
        for i, x in enumerate(nums):
            if i==0:
                dp[1]=x
            else:
                dp[i+1]= max(dp[i], dp[i-1]+x)
        return dp[n]
