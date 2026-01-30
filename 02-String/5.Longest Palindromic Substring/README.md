# 5. Longest Palindromic Substring

**Runtime:** 9940 ms  
**Beats:** 5.00%  

**Memory:** 12.51 MB  
**Beats:** 57.96%

---

## Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

A palindrome reads the same forward and backward.

---

## Examples

### Example 1
**Input:**
s = "babad"

**Output:**
"bab"

**Explanation:**  
`"aba"` is also a valid answer.

---

### Example 2
**Input:**
s = "cbbd"

**Output:**
"bb"


---

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters

---

## Solution 1: Brute Force (Your Approach)

### Approach
- Generate **all possible substrings**
- Check whether each substring is a palindrome
- Track the longest palindromic substring found

### Complexity
- **Time:** `O(n³)`  
  - `O(n²)` substrings  
  - `O(n)` palindrome check using reverse
- **Space:** `O(1)` (excluding substring creation)

### Code

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        length = 0
        left = 0
        palin = ""

        while left < len(s):
            count = 0
            for right in range(left, len(s)):
                sub = s[left:right+1]
                if sub == sub[::-1] and len(sub) > count:
                    count = len(sub)
                    if count > length:
                        palin = sub
            length = max(count, length)
            left += 1

        return palin
```
---
**Solution 2: Ideal / Optimized Solution (Expand Around Center)**
Why This Is Ideal
No need to generate all substrings

Each character (and gap) is treated as a palindrome center

Efficient and interview-preferred

Key Idea
A palindrome expands outward from its center:

Odd-length palindromes → center at a character

Even-length palindromes → center between two characters

Approach
For each index:

Expand around (i, i) → odd-length

Expand around (i, i + 1) → even-length

Track the longest valid palindrome found

Complexity
Time: O(n²)

Space: O(1)

```python
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            max_len = max(len1, len2)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]
```
---
**Comparison Summary**

Approach	Time Complexity	Space Complexity	Notes

Brute Force	O(n³)	O(1)	Easy to understand, slow

Expand Around Center	O(n²)	O(1)	Optimal, interview standard
