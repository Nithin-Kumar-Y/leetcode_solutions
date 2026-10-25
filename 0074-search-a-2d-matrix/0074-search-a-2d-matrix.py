class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        l=0
        r= m*n-1
        while l<=r:
            mid = (l+r)//2
            a= matrix[mid//n][mid%n]
            if a==target:
                return True
            elif a> target:
                r =mid-1
            else:
                l = mid+1
        return False