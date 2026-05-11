# class Solution(object):
#     def dailyTemperatures(self, temperatures):
#         """
#         :type temperatures: List[int]
#         :rtype: List[int]
#         """

#         n = len(temperatures)
#         stack = []
#         answer = [0] * n

#         for i in range(n):
#             if not stack:
#                 stack.append(i)

#             while stack and temperatures[i] > temperatures[stack[-1]]:
#                 index = stack.pop()
#                 answer[index] = i - index
#             stack.append(i)
#         return answer


# obj = Solution()
# print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


# class Solution(object):
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         currentNum = 0
#         currentString = ""
#         stack = []

#         for ch in s:
#             if ch.isdigit():
#                 currentNum = currentNum * 10 + int(ch)

#             elif ch == "[":
#                 stack.append((currentString, currentNum))
#                 currentNum = 0
#                 currentString = ""

#             elif ch.isalpha():
#                 currentString += ch

#             elif ch == "]":
#                 prevStr, num = stack.pop()
#                 currentString = prevStr + (currentString * num)

#         return currentString


# obj = Solution()
# print(obj.decodeString("3[a]2[bc]"))


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []
        splittedPath = path.split("/")

        for ch in splittedPath:

            if ch == "." or ch == "":
                continue

            if ch == "..":
                if not stack:
                    continue
                else:
                    stack.pop()

            else:
                stack.append(ch)

        return "/" if not stack else "/" + "/".join(stack)


obj = Solution()
print(obj.simplifyPath("/home//foo/"))
