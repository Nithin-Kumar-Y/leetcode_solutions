## 1209. Remove All Adjacent Duplicates in String II

**RUNTIME 59MS 51.83%**


**MEMORY  18.21MB 56.48%**


---
## SOLUTIONS
```PYTHON

class Solution(object):

    def removeDuplicates(self, s, k):

        stack = []  # (char, count)

        for ch in s:

            if stack and stack[-1][0] == ch:

                stack[-1][1] += 1

                if stack[-1][1] == k:

                    stack.pop()

            else:

                stack.append([ch, 1])

        result = ""

        for ch, count in stack:

            result += ch * count
        
        return result
```
