class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(i, path):
            res.append(path[:])
            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()
        backtrack(0, [])
        return res