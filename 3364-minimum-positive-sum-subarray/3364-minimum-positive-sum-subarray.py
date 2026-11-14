class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        best = float('inf')
        for i in range(len(nums)-l+1):
            total = 0
            leng = l
            while leng <= r and i+leng<= len(nums):
                total = sum(nums[i:i+leng])
                if total>0:
                    if total<best:
                        best = total
                leng+=1
        return best if best != float('inf') else -1