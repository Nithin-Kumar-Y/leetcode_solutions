class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans=0
        nums.sort()
        l=nums[0]
        r=nums[0]
        for i in nums:
            if r==i:
                continue
            elif r+1==i:
                r+=1
            else:
                if r-l+1> ans:
                    ans= r-l+1
                l=i
                r=i
        if r-l+1>ans:
            ans = r-l+1
        return ans