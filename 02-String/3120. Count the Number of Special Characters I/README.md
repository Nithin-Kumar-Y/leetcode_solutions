## 3120. Count the Number of Special Characters I


**RUNTIME 0MS 100%**


**MEMORY  12.36MB  87.18%**


---
```PYTHON
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        small = set()
        big = list()
        count = 0
        for i in word:
            if i.upper() == i:
                big.append(i)
            else:
                small.add(i)
        for i in small:
            count+=1 if i.upper() in big else 0
        return count
```
