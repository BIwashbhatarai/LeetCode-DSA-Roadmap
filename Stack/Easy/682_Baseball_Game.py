# 682. Baseball Game
# LeetCode Problem
# Approach: Use a stack to track valid scores.
# Operations:
#   "+" -> sum of last two scores
#   "D" -> double last score
#   "C" -> remove last score
#   number -> add to stack
# Complexity:
#   Time: O(n)
#   Space: O(n)


class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for ops in operations:
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops == "C":
                stack.pop()
            elif ops == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(ops))

        return sum(stack)


if __name__ == "__main__":
    obj = Solution()
    print(obj.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
