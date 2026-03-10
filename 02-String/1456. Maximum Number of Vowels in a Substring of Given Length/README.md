## 1456. Maximum Number of Vowels in a Substring of Given Length

**Runtime- 73ms  Beats- 94.17%**


**Memory- 15.47MB  Beats- 82.73%**

---
## SOLUTION
```PYTHON

class Solution(object):

    def maxVowels(self, s, k):

        """
        :type s: str
        :type k: int
        :rtype: int
        """

        current = 0
        best = 0
        for j in s[:k]:
            if j in "aeiou":
                current+=1
        best = current

        for i in range(len(s)-k):
            if s[i+k] in "aeiou":
                current+=1
                if best == k:
                    return k
            if s[i] in "aeiou":
                current-=1
            if current > best:
                best = current

        return best
```
