class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## fibanicco series
        if n<=1:
            return n
        prev2= 0
        prev1= 1
        for i in range(n):
            curr = prev2+ prev1
            prev2= prev1
            prev1= curr
        return prev1