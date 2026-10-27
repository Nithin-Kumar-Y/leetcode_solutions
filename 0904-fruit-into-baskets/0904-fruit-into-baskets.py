class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        seen = {}
        best=0
        curr=0
        l=0
        for i in fruits:
            seen[i] = seen.get(i, 0)+1
            curr+=1
            while len(seen)>2:
                a = fruits[l]
                seen[a]-=1
                if seen[a]==0:
                    del seen[a]
                l+=1
                curr-=1
            if curr>best:
                best  = curr
        return best