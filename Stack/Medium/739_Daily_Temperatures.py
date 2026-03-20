class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        stack = []
        index = 0
        answer = [0] * n

        for i in range(n):
            if not stack:
                stack.append(i)

            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        return answer


obj = Solution()
print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
