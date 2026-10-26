class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        best = sum(cardPoints[:k])
        curr=best
        for i in range(k):
            curr+= cardPoints[n-1-i]-cardPoints[k-i-1]
            if curr>best:
                best = curr
        return best