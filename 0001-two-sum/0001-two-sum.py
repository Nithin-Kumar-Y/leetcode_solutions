class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c = {}
        for i,x in enumerate(nums):
            if target-x in c:
                return [i, c[target-x]]
            c[x] = i
            