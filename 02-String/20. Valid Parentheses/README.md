## 20. Valid Parentheses

**Run:O(1)- 0ms- 100%**

** Space:O(n) 12.53mb- 65.67% **
---
# QUESTION:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
**Example 1:**

Input: s = "()"

Output: true

**Example 2:**

Input: s = "()[]{}"

Output: true

**Example 3:**

Input: s = "(]"

Output: false

**Example 4:**

Input: s = "([])"

Output: true

**Example 5:**

Input: s = "([)]"

Output: false
---
## SOLUTIONS:

class Solution(object):

    def isValid(self, s):
    
        """
        
        :type s: str
        
        :rtype: bool
        
        """
        
        a= []
        
        for i in s:
        
            if i in "([{":
            
                a.append(i)
                
            elif i == ")" and len(a)!=0 and a[-1]=="(" :
            
                a.pop()
                
            elif i == "]" and len(a)!=0 and a[-1]== "[" :
            
                a.pop()
                
            elif i == "}" and len(a)!=0 and a[-1] == "{" :
            
                a.pop()
                
            else:
            
                return False
                
        return len(a)==0
        
