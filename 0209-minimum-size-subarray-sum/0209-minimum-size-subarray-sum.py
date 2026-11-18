class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        best = float('inf')
        left=0
        total=0
        for right, val in enumerate(nums):
            total+=val
            while total>=target:
                total-=nums[left]
                left+=1
                if right-left+1 < best:
                    best= right-left+2
        if best==float('inf'):
            return 0
        return best