class Solution(object):
    def maxVowels(self, s, k):
        n = len(s)
        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        maxCount = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maxCount = count

        # Sliding window
        for i in range(k, n):
            if s[i - k] in vowels:
                count -= 1

            if s[i] in vowels:
                count += 1

            maxCount = max(maxCount, count)

        return maxCount


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxVowels("abciiidef", 3))  # Output: 3
