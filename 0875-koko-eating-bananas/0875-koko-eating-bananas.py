class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n= len(piles)
        low = 1
        high = max(piles)
        if n==h:
            return high
        ans = high
        while low <= high:
            m= (low+ high)//2
            total = 0
            for i in piles:
                total += (i+m-1)//m
            if total <= h:
                high = m-1
                ans = m
            else:
                low= m+1
        return ans