class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = []
        duplicate = []
        count = 0

        for char in s:
            if char in seen:
                duplicate.append(char)
            else:
                seen.append(char)
                count += 1
        return count


obj = Solution()
print(obj.lengthOfLongestSubstring("pwwkew"))
