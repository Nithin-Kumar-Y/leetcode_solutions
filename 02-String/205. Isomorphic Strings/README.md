## 205. Isomorphic Strings


**RUNTIME- 7MS 89.38%**


**MEMORY 12.68MB 99.00%**


## SOLUTIONS:
```PYTHON
class Solution(object):

    def isIsomorphic(self, s, t):

        """

        :type s: str

        :type t: str

        :rtype: bool

        """

        bill = dict()

        wow = dict()

        for i, letter in enumerate(s):

            if letter in bill:

                if t[i] != bill[letter]:

                    return False

            else:

                bill[letter] = t[i]

            if t[i] in wow:

                if wow[t[i]] != letter:

                    return False

            else:

                wow[t[i]] = letter

        return True
```
