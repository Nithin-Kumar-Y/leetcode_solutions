class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = 0
        l=0
        seen = set()
        for r in range(len(s)):
            x=s[r]
            if x not in seen:
                seen.add(x)
            else:
                while l<r and x in seen:
                    seen.discard(s[l])
                    l+=1
                seen.add(x)
            if r-l+1>best:
                best = r-l+1
        return best