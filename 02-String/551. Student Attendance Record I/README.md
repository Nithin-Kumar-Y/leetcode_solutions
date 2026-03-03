## 551. Student Attendance Record I

**RUNTIME 3MS  16.22%**

**MEMORY 12.37MB  86.24%**

---
```PYTHON

class Solution(object):
    def checkRecord(self, s):

        """
        :type s: str
        :rtype: bool
        """

        if s.count("A")>1:

            return False

        consecutive = 0

        for i in s:

            if i == "L":

                consecutive+=1

                if consecutive >=3:

                    return False

            else:

                consecutive = 0

        return True

```
