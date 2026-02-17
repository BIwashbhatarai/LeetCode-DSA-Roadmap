class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i, char in enumerate(s):
            # Skip if char already in stack
            if char in stack:
                continue

            # While the last char in stack is bigger than current char
            # and it appears later in the string, remove it
            while stack and char < stack[-1] and stack[-1] in s[i + 1 :]:
                stack.pop()

            # Append current char
            stack.append(char)

        return "".join(stack)


obj = Solution()
print(obj.removeDuplicateLetters("ssabbst"))
