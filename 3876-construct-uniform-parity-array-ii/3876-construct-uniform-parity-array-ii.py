class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        lowest_odd = float("inf")
        lowest_even = float('inf')
        for i in nums1:
            if i%2==0:
                if i< lowest_even:
                    lowest_even = i
            else:
                if i< lowest_odd:
                    lowest_odd = i
        if lowest_odd < lowest_even:
            return True
        if lowest_odd == float('inf') or lowest_even == float('inf'):
            return True
        return False