class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack = []
        result = ""

        for val in num:
            while stack and k > 0 and val < stack[-1]:
                stack.pop()
                k -= 1

            stack.append(val)

        while stack and k > 0:
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip("0")

        if not result:
            return "0"
        return result


obj = Solution()
print(obj.removeKdigits("1432219", 3))
