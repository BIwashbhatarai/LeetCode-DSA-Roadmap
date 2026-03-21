# LeetCode 394: Decode String
# Problem:
# Given an encoded string, return its decoded string.
# Encoding rule: k[encoded_string], where the encoded_string inside the square brackets is repeated k times.
# Example:
# Input: "3[a]2[bc]"
# Output: "aaabcbc"


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Initialize variables
        currentString = ""  # stores the current decoded string
        currentNumber = 0  # stores the current number (k)
        stack = []  # stack to keep track of previous strings and numbers

        # Loop through each character in the string
        for ch in s:
            if ch.isdigit():
                # Build the current number (handle multi-digit numbers)
                currentNumber = currentNumber * 10 + int(ch)

            elif ch == "[":
                # Push the current state to the stack before entering a new bracket
                stack.append((currentString, currentNumber))
                # Reset currentString and currentNumber for the new bracket
                currentString = ""
                currentNumber = 0

            elif ch.isalpha():
                # Append letters to currentString
                currentString += ch

            elif ch == "]":
                # Pop the last state from the stack and combine
                prevString, num = stack.pop()
                currentString = prevString + (currentString * num)

        # Return the fully decoded string
        return currentString


# --------------------------
# Example usage / test
# --------------------------
if __name__ == "__main__":
    obj = Solution()
    print(obj.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
    print(obj.decodeString("3[a2[c]]"))  # Output: "accaccacc"
    print(obj.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
