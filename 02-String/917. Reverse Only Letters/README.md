## 917. Reverse Only Letters


**Runtime- 1ms  Beats- 22.68%**


**Memory- 12.49MB  - Beats- 54.17%**

---
## SOLUTION
```PYTHON

class Solution(object):

    def reverseOnlyLetters(self, s):

        """
        :type s: str
        :rtype: str
        """

        l, r = 0, len(s)-1
        alph= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        ans = list(s)
        while l< r:
            while (s[l] not in alph) and l<r:
                l+=1
            while (s[r] not in alph) and l<r:
                r-=1
            ans[l], ans[r] = ans[r], ans[l]
            l+=1
            r-=1

        return "".join(ans)
```
