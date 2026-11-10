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
            if i==n:
                return 
            backtrack(i+1, path+[nums[i]])
            backtrack(i+1, path)
        backtrack(0, [])
        return res