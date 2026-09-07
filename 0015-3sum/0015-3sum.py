class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        for l in range(n-2):
            if l>0 and nums[l]== nums[l-1]:
                continue
            x = nums[l]
            m = l+1
            r= n-1
            while m<r:
                y = nums[m]
                z= nums[r]
                if x+y+z ==0:
                    res.append([x,y,z])
                    while r-1 >m and z== nums[r-1]:
                        r-=1
                    while m+1<r and y==nums[m+1]:
                        m+=1
                    m+=1
                    r-=1
                elif x+y+z > 0:
                    r-=1
                else:
                    m+=1
        return res