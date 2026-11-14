class Solution:
    def generateParenthesis(self, n):
        ans = set()
        def backtrack(i,path, total):
            if total==0:
                if len(path)==2*n:
                    ans.add(path[:])
                    return
            if total<0 or i>=2*n:
                return
            for x,y in [("(",1),(")",-1)]:
                backtrack(i+1, path+x, total+y)
        backtrack(0,"", 0)
        return list(ans)