class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total =0
        if n>=1000:
            a = min(n, 999999)-999
            total+= a
        if n>=1000000:
            a = min(n, 999999999)-999999
            total+= (a*2)
        if n>=1000000000:
            a= min(n, 999999999999)-999999999
            total+= a*3
        if n>=1000000000000:
            a= min(n, 999999999999999)-999999999999
            total+= a*4
        if n== 10**15:
            total +=5
        return total