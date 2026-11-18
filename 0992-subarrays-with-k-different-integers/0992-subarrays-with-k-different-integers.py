class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(k):
            count=0
            left=0
            seen={}
            for right, val in enumerate(nums):
                seen[val]= seen.get(val, 0)+1
                while len(seen)>k:
                    a= nums[left]
                    seen[a]-=1
                    if seen[a]==0:
                        del seen[a]
                    left+=1
                count+= right-left+1
            return count
        return atmost(k)-atmost(k-1)
            