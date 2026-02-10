# Longest Repeating Character Replacement (Sliding Window + HashMap)
class Solution(object):
    def characterReplacement(self, s, k):
        """
        Find the length of the longest substring where at most k letters
        can be replaced to make all characters the same.

        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        mappingDictionary = {}  # counts of letters in current window
        maxFreqency = 0  # frequency of the most common letter
        maxLength = 0  # maximum valid window length

        for right in range(len(s)):
            # Add current character to dictionary
            mappingDictionary[s[right]] = mappingDictionary.get(s[right], 0) + 1

            # Update max frequency of any character in the window
            maxFreqency = max(mappingDictionary.values())

            # Calculate window size and replacements needed
            windowSize = right - left + 1
            requirementNeeded = windowSize - maxFreqency

            # Shrink window from left if replacements exceed k
            while requirementNeeded > k:
                mappingDictionary[s[left]] -= 1
                left += 1
                windowSize = right - left + 1
                requirementNeeded = windowSize - maxFreqency

            # Update max length of valid window
            maxLength = max(maxLength, windowSize)

        return maxLength


# Example usage
obj = Solution()
print(obj.characterReplacement("ABAB", 2))  # Output: 4
