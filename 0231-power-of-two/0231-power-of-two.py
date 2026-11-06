class Solution(object):
    def isPowerOfTwo(self, n):
        b=1
        while b<=n:
            if b==n:
                return True
            b= b<<1
        return False