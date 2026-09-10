class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = k
        while True:
            if ans in nums:
                ans+= k
            else:
                return ans
        return ans