## 557. Reverse Words in a String III

**Runtime- 3ms  64.87%**

**Memory- 12.93mb 66.72%**
---
## SOLUTION:
```python
class Solution(object):

    def reverseWords(self, s):

        """

        :type s: str

        :rtype: str

        """

        s = list(map(str, s.split()))

        ans = ""

        for i in s:

            if ans == "":

                ans = i[::-1]

            else:

                ans = ans + " "+ i[::-1]

        return ans
```
