class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n= len(grid[0]) #col
        m= len(grid) #row
        best = grid[0][0]

        dir= [(0,1),(0,-1),(1,0),(-1,0)]
        def backtrack(r, c, curr, best):
            if r<0 or r>=m or c<0 or c>=n:
                return best
            val= grid[r][c]
            if val== 0:
                return curr
            grid[r][c]= 0
            curr+=val
            for x,y in dir:
                if curr>best:
                    best=curr
                a= backtrack(r+x, y+c, curr, best)
                if a>best:
                    best= a
            grid[r][c]=val
            return best
        for r in range(m):
            for c in range(n):
                if grid[r][c] !=0:
                    a= backtrack(r, c, 0, best)
                    if a>best:
                        best=a
        return best






        ## Not falling below man
        """
        ans= [[0]*n for _ in range(m)]
        for i in range(n):
            ans[0][i]=grid[0][i]
        for i in range(1, m):
            for j in range(n):
                if j==0 :
                    ans[i][j]= max(ans[i-1][j], ans[i-1][j+1]) + grid[i][j]
                elif j==len(grid[0])-1:
                    ans[i][j]=max(ans[i-1][j], ans[i-1][j-1])+ grid[i][j]
                else:
                    ans[i][j]=max(ans[i-1][j], ans[i-1][j-1], ans[i-1][j+1])+ grid[i][j]
            print(ans)
        return max(ans[m-1])
        """