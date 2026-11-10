class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n=len(nums)
        def backtrack(i, path):
            if path not in res:
                res.append(path[:])
            for k in range(i, n):
                backtrack(k+1, path+[nums[k]])
                backtrack(k+1, path)
        backtrack(0, [])
        return res