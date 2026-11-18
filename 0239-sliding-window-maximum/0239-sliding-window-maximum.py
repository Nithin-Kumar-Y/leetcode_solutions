from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        order=deque()
        left=0
        ans=[]
        for right, val in enumerate(nums):
            while order and order[-1]<val:
                order.pop()
            order.append(val)
            if right<k-1:
                continue
            ans.append(order[0])
            if nums[left]==order[0]:
                order.popleft()
            left+=1
        return ans