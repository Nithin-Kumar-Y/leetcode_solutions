## 541.Reverse String II

**Runtime-0ms Beats-100.00%**

**Memory-12.75MB Beats-44.61%**
---

### SOLUTION:
```python
class Solution(object):

    def reverseStr(self, s, k):

        """

        :type s: str

        :type k: int

        :rtype: str

        """

        if len(s)<=k:

            return s[::-1]

        slow,fast = 0, k

        reverse = 1

        turn = len(s)//k

        temp = []

        for i in range(turn):

            if reverse == 1:

                steel = s[slow:fast]

                temp.append(steel[::-1])

            else:

                temp.append(s[slow:fast])

            reverse*=(-1)

            slow+=k

            fast+=k

        if reverse == -1:

            temp.append(s[slow:])

        else:

            temp.append(s[slow:][::-1])

        return "".join(temp)
```
