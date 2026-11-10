class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        def backtrack(path, i, total):
            if len(path)==k:
                if total==0:
                    ans.append(path)
                return
            for j in range(i, 10):
                if total<i:
                    break
                backtrack(path+[j], j+1, total-j)
        backtrack([], 1, n)
        return ans