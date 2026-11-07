class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        stack = []
        seen = {}
        for i in nums2[::-1]:
            while stack and stack[-1]<=i:
                stack.pop()
            if not stack:
                seen[i]=-1
            else:
                seen[i]= stack[-1]
            stack.append(i)
        for i in nums1:
            ans.append(seen[i])
        return ans