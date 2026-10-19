class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        pos=0  
        neg=0
        n= len(nums)
        sign = 1
        for r in range(n):
            if sign ==1:
                while pos<n and nums[pos]<=0 :
                    pos+=1
                ans.append(nums[pos])
                pos+=1
            else:
                while neg<n and nums[neg]>=0 :
                    neg+=1
                ans.append(nums[neg])
                neg+=1
            sign*= -1
        return ans