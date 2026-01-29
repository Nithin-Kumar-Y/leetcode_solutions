## 67. Add Binary 

**Runtime:O(1)- 9ms- 16.05%**

**Space: O(n)- 12.4- 57.20%**

---
## QUESTION:

Given two binary strings a and b, return their sum as a binary string.

**Example 1:**

Input: a = "11", b = "1"

Output: "100"

**Example 2:**

Input: a = "1010", b = "1011"

Output: "10101"
---
## SOLUTIONS:

class Solution(object):

    def addBinary(self, a, b):
    
        if a =="0":
        
            return b
            
        elif b =="0":
        
            return a
            
        a_s, b_s = str(a), str(b)
        
        a,b = 0,0
        
        for i in range(len(a_s)):
        
            a+=(int(a_s[i])*2**(len(a_s)-i-1))
            
        for i in range(len(b_s)):
        
            b+=(int(b_s[i])*2**(len(b_s)-i-1))
            
        suma =a+b
        
        st = ""
        
        while True:
        
            v = suma %2
            
            st= str(int(v)) + st
            
            suma = suma//2
            
            if suma == 0:
            
                break
                
        return st

## Ideal Solution:  0ms

class Solution(object):

    def addBinary(self, a, b):
    
        """
        
        :type a: str
        
        :type b: str
        
        :rtype: str
        
        """
        
        return bin(int(a, 2) + int(b, 2))[2:]
  
