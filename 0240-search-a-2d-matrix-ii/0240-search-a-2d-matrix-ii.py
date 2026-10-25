class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        i=0
        j= col-1
        while j>=0 and i<row:
            a= matrix[i][j]
            if a==target:
                return True
            if a>target:
                j-=1
            else:
                i+=1
        return False