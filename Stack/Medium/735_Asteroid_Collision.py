class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for ast in asteroids:
            alive = True

            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) > stack[-1]:
                    stack.pop()
                elif stack[-1] > abs(ast):
                    alive = False
                    break
                else:
                    stack.pop()
                    alive = False
                    break

            if alive:
                stack.append(ast)

        return stack


# ✅ Test cases
obj = Solution()
print(obj.asteroidCollision([5, 10, -5]))
print(obj.asteroidCollision([8, -8]))
print(obj.asteroidCollision([10, 2, -5]))
print(obj.asteroidCollision([5, -5, -10]))
