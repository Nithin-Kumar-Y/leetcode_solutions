## 1652. Defuse the Bomb

**Runtime- 0ms  Beats- 100.00%**


**Memory- 12.32MB  Beats- 88.24%**

---
## SOLUTION
```PYTHON

class Solution(object):
    def decrypt(self, code, k):

        n = len(code)

        if k == 0:
            return [0] * n

        ans = [0] * n

        if k > 0:
            total = sum(code[1:k+1])

            for i in range(n):
                ans[i] = total
                total -= code[(i+1) % n]
                total += code[(i+k+1) % n]

        else:
            k = -k
            total = sum(code[n-k:])

            for i in range(n):
                ans[i] = total
                total -= code[(i-k+n) % n]
                total += code[i % n]

        return ans
```
