class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(n):
            if freq[s[i]] == 1:
                return i
        return -1


obj = Solution()
print(obj.firstUniqChar("hikinghorse"))
