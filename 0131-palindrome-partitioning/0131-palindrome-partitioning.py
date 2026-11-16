class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans=[]
        path=[]
        n=len(s)
        def isPalind(l, r):
            while l< r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(start):
            if start==n:
                ans.append(path[:])
                return
            for end in range(start, n):
                if isPalind(start, end):
                    path.append(s[start:end+1])
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return ans