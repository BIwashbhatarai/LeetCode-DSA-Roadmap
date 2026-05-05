class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        seen = set()
        maxLen = 0
        n = len(s)

        for j in range(n):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxLen = max(maxLen, j - i + 1)

        return maxLen
