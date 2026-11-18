class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        best = len(nums)+1
        left=0
        total=0
        for right, val in enumerate(nums):
            total+=val
            while total>=target:
                if right-left+1 < best:
                    best= right-left+1
                total-=nums[left]
                left+=1
        if best==len(nums)+1:
            return 0
        return best