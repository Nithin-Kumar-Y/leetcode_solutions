class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums)-1
        for i in nums:
            if i!=0:
                nums[l]= i
                l+=1
        for i in range(len(nums)-l):
            nums[l+i]=0
        return nums
