class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=max(nums)
        r=sum(nums)
        ans =-1
        while l<=r:
            mid = (l+r)//2
            turn=1
            total=0
            for i in nums:
                if total+i<=mid:
                    total+=i
                else:
                    turn+=1
                    total=i
            if turn <= k:
                ans =mid
                r=mid-1
            else:
                l=mid+1
        return ans