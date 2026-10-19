class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return []
        ans = []
        nums.sort()
        for i,x in enumerate(nums):
            if x==target:
                ans.append(i)
        return ans