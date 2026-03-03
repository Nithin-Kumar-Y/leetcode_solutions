## 1047. Remove All Adjacent Duplicates In String

**RUNTIME 39MS  58.22%**

**MEMORY 13.61MB   26.36%**


---
## SOLUTIONS

```PYTHON
class Solution(object):
    def removeDuplicates(self, s):

        """
        :type s: str
        :rtype: str
        """

        ans = list()
        for i in s:
            if not ans:
                ans.append(i)
            else:
                if ans[-1]==i:
                    ans.pop()
                else:
                    ans.append(i)

        return "".join(ans)
```
