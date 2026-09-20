class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = "zyxwvutsrqponmlkjihgfedcba"
        total=0
        for i,x in enumerate(s):
            total+= (seen.index(x)+1)*(i+1)
        return total