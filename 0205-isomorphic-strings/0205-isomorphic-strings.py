class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a= {}
        b={}
        for i in range(len(s)):
            x= s[i]
            y = t[i]
            if x not in a:
                if y in b:
                    return False
            else:
                if a[x] != y:
                    return False
            a[x]=y
            b[y]=x

        return True