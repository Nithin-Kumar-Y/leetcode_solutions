class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0

        for i in range(len(s)):
            
            res+=(i+1)*(26-(ord(s[i])-97))
        return res