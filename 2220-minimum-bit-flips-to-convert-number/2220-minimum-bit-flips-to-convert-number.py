class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        c=0
        a= start
        b= goal
        while a>0 or b>0:
            if (a&1)==0:
                if (b&1) !=0:
                    c+=1
            else:
                if (b&1) != 1:
                    c+=1
            a= a>>1
            b = b>>1
        return c