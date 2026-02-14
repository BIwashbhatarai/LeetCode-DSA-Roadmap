# 1047. Remove All Adjacent Duplicates in String


class Solution(object):
    """
    Solution to remove all adjacent duplicates in a string using stack.
    """

    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char != stack[-1]:
                    stack.append(char)
                else:
                    stack.pop()

        return "".join(stack)


# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.removeDuplicates("azxxzy"))  # Output: "ay"
    print(obj.removeDuplicates("abbaca"))  # Output: "ca"
