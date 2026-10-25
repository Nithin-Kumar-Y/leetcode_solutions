class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n=len(bloomDay)
        l=0
        r=max(bloomDay)
        ans = -1
        while l<=r:
            mid = (l+r)//2
            bloomed =0
            count = 0
            i=0
            while i<n:
                if bloomDay[i]<=mid:
                    count+=1
                else:
                    count=0
                i+=1
                if count==k:
                    bloomed+=1
                    count=0
            if bloomed>=m:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans