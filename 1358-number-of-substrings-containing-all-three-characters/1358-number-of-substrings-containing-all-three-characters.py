class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        l=0
        seen = {}
        n=len(s)
        for r, x in enumerate(s):
            seen[x]=seen.get(x,0)+1
            if len(seen)==3:
                ans+=n-r
                while len(seen)==3:
                    a=s[l]
                    seen[a]-=1
                    if seen[a]==0:
                        del seen[a]
                    else:
                        ans+=n-r
                    l+=1
                
        return ans