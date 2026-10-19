class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            a= nums[i]
            l=i+1
            r=n-1
            while l<r:
                b = nums[l]
                c=nums[r]
                if a+b+c==0:
                    if (a, b,c) not in ans:
                        res.append([a,b,c])
                        ans.add((a,b,c))
                    l+=1
                    r-=1
                elif a+b+c>0:
                    r-=1
                else:
                    l+=1
        return res