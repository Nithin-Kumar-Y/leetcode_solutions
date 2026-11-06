class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b=1
        while b<=n:
            if b==n:
                return True
            b= b<<2
        return False