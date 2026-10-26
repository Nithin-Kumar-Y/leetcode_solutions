class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        best = 0
        curr=0
        seen = 0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                while seen==k:
                    if nums[l]==0:
                        seen-=1
                    curr-=1
                    l+=1
                seen+=1
            curr+=1
            if curr>best:
                best = curr
        return best