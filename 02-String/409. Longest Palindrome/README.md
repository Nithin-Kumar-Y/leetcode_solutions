## 409. Longest Palindrome

**Runtime- 3ms Beats-73.75%**

**Memory-12.51MB Beats-26.87%**

---
## SOLUTION
```PYTHON
from collections import Counter

class Solution(object):

    def longestPalindrome(self, s):

        counts = Counter(s)

        ans = 0

        has_odd = False

        for freq in counts.values():

            ans += (freq // 2) * 2

            if freq % 2 == 1:

                has_odd = True

        return ans + (1 if has_odd else 0)

```
