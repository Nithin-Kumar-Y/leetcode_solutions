## 438. Find All Anagrams in a String

**RUNTIME- 115MS   22.98%**


**MEMORY  13.22MB  86%**


---
## SOLUTIONS
```PYTHON

class Solution(object):

    def findAnagrams(self, s, p):

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        from collections import Counter

        m = len(p)
        n = len(s)
        ans = []
        c = Counter(s[:m])
        c_p = Counter(p)
        if c ==c_p:
            ans.append(0)
        for i in range(1, n-m+1):
            c[s[i+m-1]] +=1
            c[s[i-1]] -=1

            if c[s[i-1]] ==0:
                del c[s[i-1]]
            
            if c == c_p:
                ans.append(i)

        return ans
