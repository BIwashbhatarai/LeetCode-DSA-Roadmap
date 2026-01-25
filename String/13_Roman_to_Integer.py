# Intuition
# Each Roman numeral has a value. Normally we add values left to right,
# but if a smaller numeral comes before a larger one, we subtract it.
# Example: "IV" → 1 before 5 → subtract 1 → 4

# Approach
# 1. Create a dictionary mapping Roman symbols to integer values.
# 2. Loop through the string from index 0 to n-2:
#    - Compare current and next value.
#    - If current < next, subtract current from total.
#    - Else, add current to total.
# 3. Add the last value to total (since it’s never checked in the loop).
# 4. Return total.

# Complexity
# - Time complexity: O(n), where n = length of the string
# - Space complexity: O(1), dictionary has fixed size


class Solution(object):
    def romanToInt(self, s):
        romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        n = len(s)

        for i in range(n - 1):
            currentValue = romanMap[s[i]]
            nextValue = romanMap[s[i + 1]]

            if currentValue < nextValue:
                total -= currentValue
            else:
                total += currentValue

        total += romanMap[s[-1]]
        return total
