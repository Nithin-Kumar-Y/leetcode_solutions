## 520. Detect Capital


**RUNTIME 0MS 100%**


**MEMORY 12.36MB  85.28%**

---
## SOLUTIONS
```PYTHON
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        prev = None
        for i in range(len(word)):
            if i ==0:
                prev = "small" if word[i] in "abcdefghijklmnopqrstuvwxyz" else "cap"
            else:
                if word[i] not in "abcdefghijklmnopqrstuvwxyz" and prev is "small":
                    return False
                elif word[i] in "abcdefghijklmnopqrstuvwxyz" :
                    if prev is "cap" and count>1:
                        return False
                    prev = "small"
                else:
                    prev = "cap"
            
            count+=1
        return True
```
