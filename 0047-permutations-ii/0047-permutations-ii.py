class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        used = [False]*(len(nums))
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and used[i-1]==False:
                    continue
                used[i]= True
                backtrack(path+[nums[i]])
                used[i] = False
        backtrack([])
        return res