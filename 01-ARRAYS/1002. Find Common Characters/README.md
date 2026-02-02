## 1002. Find Common Characters

**Runtime- 11ms- 87.14%**

**Space: 12.38mb - 97.33%**

---
### SOLUTION:
```PYTHON
class Solution(object):

    def commonChars(self, words):

        if not words:

            return []

        ans = list(words[0])

        for i in range(1, len(words)):

            words[i] = list(words[i])

            temp = []

            for j in ans:

                if j in words[i]:

                    temp.append(j)

                    words[i].remove(j)

            ans = temp

        return ans
```
