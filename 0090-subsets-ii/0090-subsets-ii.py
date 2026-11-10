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
            res.append(path[:])

            for k in range(i, n):
                a= nums[k]
                if k>i and a==nums[k-1]:
                    continue
                #path.append(a)
                backtrack(k+1, path+[a])
                #path.pop()
        backtrack(0, [])
        return res