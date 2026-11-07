class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in nums[::-1]:
            while stack and stack[-1]<=i:
                stack.pop()
            stack.append(i)
        ans =[]
        for i in nums[::-1]:
            while stack and stack[-1]<=i:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(i)
        return ans[::-1]