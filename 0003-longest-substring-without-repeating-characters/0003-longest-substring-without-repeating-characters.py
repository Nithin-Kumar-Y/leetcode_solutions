class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = 0
        l=0
        curr=0
        seen = set()
        for r in range(len(s)):
            x=s[r]
            if x not in seen:
                seen.add(x)
                curr+=1
            else:
                while x in seen:
                    seen.discard(s[l])
                    l+=1
                    curr-=1
                seen.add(x)
                curr+=1
            if curr>best:
                best = curr
        return best