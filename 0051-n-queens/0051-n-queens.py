class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans=[]
        board=[["."]*n for _ in range(n)]
        cols = set()
        diag1= set()
        diag2= set()
        def backtrack(i): #row
            if i==n:
                ans.append(["".join(i) for i in board])
                return
            for col in range(n):
                if (col in cols )|( i-col in diag1 )|( i+col in diag2):
                    continue

                cols.add(col)
                diag1.add(i-col)
                diag2.add(i+col)
                board[i][col]= "Q"

                backtrack(i+1)

                board[i][col]="."
                cols.remove(col)
                diag1.remove(i-col)
                diag2.remove(i+col)
        backtrack(0)
        return ans