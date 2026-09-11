class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        seen = set()
        for i, x in enumerate(digits):
            for j, y in enumerate(digits):
                for k,z in enumerate(digits):
                    if i == j or i==k or k==j or z%2==1 or x==0:
                        continue
                    num = x*100+ y*10+z
                    seen.add(num)
        return len(seen)