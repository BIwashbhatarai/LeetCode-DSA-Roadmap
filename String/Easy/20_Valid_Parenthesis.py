"""
Title: Valid Parentheses – Stack Approach
Description:
Check if a string containing '(', ')', '{', '}', '[' and ']' is valid.
A string is valid if every opening bracket has a corresponding closing bracket in the correct order.
Approach: Use a stack to keep track of opening brackets and match them with closing brackets.
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Mapping of closing to opening brackets
        bracketMapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in "({[":  # Opening bracket → push to stack
                stack.append(char)
            else:  # Closing bracket → check with stack
                if len(stack) == 0:  # Nothing to match with
                    return False
                if stack[-1] == bracketMapping[char]:  # Matches top of stack
                    stack.pop()  # Pop the matched opening bracket
                else:  # Mismatch
                    return False

        # If stack is empty → all brackets matched
        return len(stack) == 0


# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.isValid("()"))  # True
    print(obj.isValid("()[]{}"))  # True
    print(obj.isValid("(]"))  # False
    print(obj.isValid("([)]"))  # False
    print(obj.isValid("{[]}"))  # True
