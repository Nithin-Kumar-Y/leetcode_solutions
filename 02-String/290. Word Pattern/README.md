## 290. WORD PATTERN

**RUNTIME 0MS- 100%**


**MEMORY 12.48MB 57.98%**


---
## SOLUTIONS

```PYTHON
class Solution(object):

    def wordPattern(self, pattern, s):

        """

        :type pattern: str

        :type s: str

        :rtype: bool

        """

        s = list(s.split())

        bill = dict()

        wow = set()

        if len(s) != len(pattern):

            return False

        for i, letter in enumerate(pattern):

            if letter not in bill :

                if s[i] in wow:

                    return False

                else:

                    wow.add(s[i])

                bill[letter]= s[i]

            else:

                if bill[letter] == s[i]:

                    pass

                else:

                    return False

        return True
```
