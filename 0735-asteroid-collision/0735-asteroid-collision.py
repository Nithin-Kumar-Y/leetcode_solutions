class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for i in asteroids[::-1]:
            if not stack:
                stack.append(i)
                continue
            while stack:
                if i>0 and stack[-1]<0:
                    if i>abs(stack[-1]):
                        stack.pop()
                        if not stack:
                            stack.append(i)
                            break
                    elif i==abs(stack[-1]):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(i)
                    break
        return stack[::-1]