class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(nums)
        visited= [False]*n
        def backtrack(path):
            if len(path)==n:
                ans.append(path[:])
                return
            for j in range(n):
                if visited[j]:
                    continue
                visited[j]=True
                backtrack(path+[nums[j]])
                visited[j]=False
        backtrack([])
        return ans