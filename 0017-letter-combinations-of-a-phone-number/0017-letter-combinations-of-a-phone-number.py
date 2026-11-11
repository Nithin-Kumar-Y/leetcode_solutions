class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans=[]
        n=len(digits)
        nums = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def backtrack(path, i):
            if len(path)==n:
                ans.append(path)
                return
            for j in nums[int(digits[i])-2]:
                backtrack(path+j, i+1)
        backtrack("", 0)
        return ans