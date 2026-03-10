## 424. Longest Repeating Character Replacement

**RUNTIME  = 135MS  73.90%**


**MEMORY 15.43MB   48.20%**


---
## SOLUTIONS
```PYTHON

class Solution(object):

    def characterReplacement(self, s, k):

        """
        :type s: str
        :type k: int
        :rtype: int
        """

        c = dict()
        best = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            if s[r] not in c:
                c[s[r]]=1
            else:
                c[s[r]]+=1
            max_freq = max(max_freq, c[s[r]])
            while (r-l+1)-max_freq >k:
                c[s[l]]-=1
                l+=1
            best = max(best, r-l+1)

        return best
```
