## 2129. Capitalize the Title

**RUNTIME 0MS 100%**

**MEMORY 12.47MB 58.56%**

---
## SOLUTIONS
```PYTHON
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = []
        for i in title.split():
            if len(i)>2:
                words.append(i.capitalize())
            else:
                words.append(i.lower())
        return " ".join(words)
```
