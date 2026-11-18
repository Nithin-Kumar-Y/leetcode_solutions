class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        count=0
        prod=1
        for right, x in enumerate(nums):
            prod*=x
            while left<= right and prod>=k:
                prod//=nums[left]
                left+=1
            count+= right-left+1
        return count