class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in reversed(s):
            if i=="(":
                curr= []
                while stack[-1] !=")":
                    curr.append(stack.pop())
                stack.pop()
                stack = stack + curr
            else:
                stack.append(i)
        return "".join(stack[::-1])