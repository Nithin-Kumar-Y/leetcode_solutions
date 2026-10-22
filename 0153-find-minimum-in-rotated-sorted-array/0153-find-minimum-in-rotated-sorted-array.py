class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l=0
        r=n-1
        while l<r:
            if nums[l]<nums[r]:
                break
            m=(l+r)//2
            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m
        return nums[l]