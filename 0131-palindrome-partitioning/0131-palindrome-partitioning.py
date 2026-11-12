class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n=len(s)
        ans=[]
        def backtrack(path, idx):
            if idx==n:
                ans.append(path[:])
                return
            for end in range(idx, n):
                a= s[idx:end+1]
                if a==a[::-1]:
                    backtrack(path+[a], end+1)
        backtrack([], 0)
        return ans