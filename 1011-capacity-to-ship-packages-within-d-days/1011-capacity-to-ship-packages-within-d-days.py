class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l=max(weights)
        r=sum(weights)
        ans = r
        while l<=r:
            m=(l+r)//2
            day=1
            total=0
            for i in weights:
                if total+i<=m:
                    total+=i
                else:
                    day+=1
                    total=i
            if day<=days:
                ans = m
                r=m-1
            else:
                l=m+1
        return ans