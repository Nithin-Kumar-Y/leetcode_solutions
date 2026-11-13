class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = set()
        diag1= set()
        diag2= set()
        def backtrack(i):
            if i==n:
                return 1
            count=0
            for j in range(n):
                if (j not in cols and i-j not in diag1 and i+j not in diag2):
                    cols.add(j)
                    diag1.add(i-j)
                    diag2.add(i+j)
                    count+= backtrack(i+1)

                    cols.remove(j)
                    diag1.remove(i-j)
                    diag2.remove(i+j)
            return count
        return backtrack(0)
            