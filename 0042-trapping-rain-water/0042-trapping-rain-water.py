class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        n = len(height)
        r= n-1
        water = 0
        l_max = height[l]
        r_max = height[r]
        while l<r:
            if r_max>= l_max:
                if l!=0:
                    water+= l_max - height[l]
                l+=1
                if l<r:
                    if height[l]> l_max:
                        l_max = height[l]
                else:
                    break

            else: ## l_max > r_max
                if r!=n-1:
                    water += r_max- height[r]
                r-=1
                if r>l:
                    if height[r]> r_max:
                        r_max = height[r]
                else:
                    break
        return water