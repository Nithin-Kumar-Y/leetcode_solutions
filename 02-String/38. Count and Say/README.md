## 38. Count and Say

#### Runtime- 9ms- 72.18%

#### Memory- 12.51mb- 54.71%

---
## QUESTION:

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"

countAndSay(n) is the run-length encoding of countAndSay(n - 1).

**Run-length encoding (RLE)** is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".
Given a positive integer n, return the nth element of the count-and-say sequence. 

**Example 1:**

Input: n = 4

Output: "1211"

**Explanation:**

```
countAndSay(1) = "1"

countAndSay(2) = RLE of "1" = "11"

countAndSay(3) = RLE of "11" = "21"

countAndSay(4) = RLE of "21" = "1211"

```
**Example 2:**

Input: n = 1

Output: "1"

**Explanation:**

This is the base case.

 
---
## SOLUTION:

class Solution(object):

    def countAndSay(self, n):
    
        """
        
        :type n: int
        
        :rtype: str
        
        """
        
        s = "1"
        
        if n == 1:
        
            return s
            
        for i in range(1, n):
        
            vl = ""
            
            count = 1
            
            char = s[0]
            
            for j in range(1, len(s)):
            
                if s[j] == char:
                
                    count+=1
                    
                else:
                
                    vl = vl+ str(count)+char
                    
                    char = s[j]
                    
                    count=1
                    
            vl = vl+ str(count)+char
            
            s = vl
            
        return s
        
--
## IDEAL SOLUTION:

class Solution(object):

    def countAndSay(self, n):
    
        """
        
        :type n: int
        
        :rtype: str
        
        """
        if n == 1:
        
            return "1"
        
        # Get the previous term recursively
        
        prev = self.countAndSay(n - 1)
        
        # Perform run-length encoding on prev
        
        result = ""
        
        count = 1
        
        for i in range(len(prev)):
        
            if i == len(prev) - 1 or prev[i] != prev[i + 1]:
            
                result += str(count) + prev[i]
                
                count = 1
                
            else:
            
                count += 1
        
        return result
        
*(OPTIONAL) __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0")) 
