class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if string t is an anagram of string s.
        :param s: First string
        :param t: Second string
        :return: True if t is an anagram of s, False otherwise
        """
        if len(s) != len(t):
            return False

        frequency = {}

        # Count characters in s
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        # Subtract characters using t
        for char in t:
            if char not in frequency or frequency[char] == 0:
                return False
            frequency[char] -= 1

        return True


# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.isAnagram("anagram", "nagaram"))  # True
    print(obj.isAnagram("rat", "car"))  # False
