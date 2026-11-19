class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n1 = len(s)
        n2 = len(t)
        if n1==0 or n2==0 or n2>n1:
            return ""
        ct= {}
        for i in t:
            ct[i] = ct.get(i,0)+1
        seen = {}
        best = n1+1
        starting_index=0
        left=0
        found = len(ct)
        for right, x in enumerate(s):
            if x in ct:
                seen[x] = seen.get(x, 0)+1
                if seen[x]==ct[x]:
                    found-=1
            while found==0:
                if found==0:
                    if right-left+1 < best:
                        best = right-left+1
                        starting_index= left
                a = s[left]
                if a in ct:
                    seen[a]-=1
                    if seen[a]<ct[a]:
                        found+=1
                left+=1
        return s[starting_index: starting_index+ best] if best != n1+1 else ""