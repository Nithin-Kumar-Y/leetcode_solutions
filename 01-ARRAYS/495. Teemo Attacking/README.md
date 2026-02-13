## 495. Teemo Attacking

**Runtime- 11ms  91.06%**

**Space 13.22mb  55.96%**
---

## SOLUTIONS
```PYTHON

class Solution(object):

    def findPoisonedDuration(self, timeSeries, duration):

        """

        :type timeSeries: List[int]

        :type duration: int

        :rtype: int

        """

        damage = 0

        for i in range(len(timeSeries)-1):

            if timeSeries[i+1]-timeSeries[i] < duration:

                damage += (timeSeries[i+1]-timeSeries[i])

            else:

                damage += duration

        damage+=duration

        return damage
```
