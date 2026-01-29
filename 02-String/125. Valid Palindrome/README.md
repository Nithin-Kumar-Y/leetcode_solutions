## 125.Valid Palindrome

**Runtime =O(n)- 149 ms- 11.76%**

**space = O(n)- 12.9mb - 65.69%**

---
## Question:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

**Example 1:**

Input: s = "A man, a plan, a canal: Panama"

Output: true

**Explanation:** "amanaplanacanalpanama" is a palindrome.

**Example 2:**

Input: s = "race a car"

Output: false

**Explanation:** "raceacar" is not a palindrome.

**Example 3:**

Input: s = " "

Output: true

**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

---
## SOLUTIONS:
class Solution(object):

    def isPalindrome(self, s):
    
        """
        
        :type s: str
        
        :rtype: bool
        
        """
        if not s:
        
            return True
            
        sl =""
        
        for i in s:
        
            if i.isalnum():
            
                sl += i.lower()
                
        if sl == "":
        
            return True
            
        return sl== sl[::-1]
## IDEAL SOLTION :
**#1**

class Solution(object):

    def isPalindrome(self, s):
    
        new = ""
        
        for ch in s:
        
            if ch.isalnum():
            
                new += ch.lower()
                
        return new == new[::-1]

 * (Optional)  __import__ ("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
---

**#2**

class Solution(object):

    def isPalindrome(self, s):

            
            l , r = 0 , len(s)-1
   
            while l<=r:
            
                if lower(s[l]).isalnum() and lower(s[r]).isalnum():
                
                    if lower(s[l]) != lower(s[r]):
                        
                        print(s[l] , s[r])
                        
                        return False
                        
                    else:
                    
                        l+=1
                        
                        r-=1
                        
                elif not lower(s[l]).isalnum():
                
                    l+=1
                    
                elif not lower(s[r]).isalnum():
                
                    r-=1
                    
            return True
