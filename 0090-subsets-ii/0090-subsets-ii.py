class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n=len(nums)
        def backtrack(i, path):
            if path not in res:
                res.append(path)
            for k in range(i, n):
                a= nums[k]
                if k>i and k==nums[k-1]:
                    continue
                backtrack(k+1, path+[a])
                backtrack(k+1, path)
        backtrack(0, [])
        return res