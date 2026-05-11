class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    stack.append(int(num1 + num2))
                elif token == "-":
                    stack.append(int(num1 - num2))
                elif token == "*":
                    stack.append(int(num1 * num2))
                elif token == "/":
                    stack.append(int(float(num1) / num2))
            else:
                stack.append(int(token))
        return stack[-1]


obj = Solution()
print(obj.evalRPN(["2", "1", "+", "3", "*"]))
