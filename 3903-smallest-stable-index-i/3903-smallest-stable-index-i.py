class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = [0]
        mini = [float('inf')]
        for i in nums:
            if i> maxi[-1]:
                maxi.append(i)
            else:
                maxi.append(maxi[-1])
        
        for i in reversed(nums):
            if i< mini[-1]:
                mini.append(i)
            else:
                mini.append(mini[-1])
        mini = mini[::-1]
        for i in range(len(nums)):
            if maxi[i+1]-mini[i] <=k:
                return i
        return -1