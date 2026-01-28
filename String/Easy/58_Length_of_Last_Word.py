class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastWord = s.split()[-1]
        return len(lastWord)
