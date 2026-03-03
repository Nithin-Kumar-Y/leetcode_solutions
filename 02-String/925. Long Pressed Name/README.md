##  925. Long Pressed Name


**RUNTIME - 0MS 100%**

**MEMEORY-  12.33MB  88.42%**


---
## SOLUTIONS

```PYTHON
class Solution(object):

    def isLongPressedName(self, name, typed):

        """
        :type name: str
        :type typed: str
        :rtype: bool
        """

        name_indx = 0
        typed_indx= 0
        if len(name) > len(typed):
            return False
        for i in typed:
            if name_indx == len(name):
                name_indx = len(name)-1
            if i == name[name_indx]:
                name_indx+=1
            elif i != name[name_indx]:
                if typed_indx> 0 and i == typed[typed_indx-1]:
                    pass
                else:
                    return False
            typed_indx +=1

        return True if name_indx == len(name) else False
```
