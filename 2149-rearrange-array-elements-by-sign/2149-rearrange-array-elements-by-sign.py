class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=0  
        neg=1
        n= len(nums)
        ans = [0]*n
        for r in range(n):
            if nums[r]>0:
                ans[pos]=nums[r]
                pos+=2
            else:
                ans[neg]=nums[r]
                neg+=2
        return ans