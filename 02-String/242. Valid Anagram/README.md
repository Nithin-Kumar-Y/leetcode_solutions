# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
chech whether counts are matching?

# Approach
    Just tried to find and list the uniqye letters, then count in both 's' and 't' strings. finally if the count doen't match return false

# Complexity
- Time complexity:O(n)- but 3ms runtime
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(1)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python []
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        low = set(s)
        for i in low:
            if t.count(i)!= s.count(i):
                return False
        return True
        
```
All suggestions are welcomed from seniorsa nad juniors too..
