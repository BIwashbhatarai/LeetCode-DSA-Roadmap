"""
Title: Group Anagrams
Description:
Given an array of strings, group the anagrams together.
An Anagram is a word formed by rearranging the letters of another word.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Author: Your Name
Date: YYYY-MM-DD
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups an array of strings into lists of anagrams.

        :param strs: List[str] - List of input strings
        :return: List[List[str]] - List of anagram groups
        """
        # Dictionary to store groups with sorted word as key
        mappingDictionary = {}

        for word in strs:
            # Sort the characters in the word to get a signature key
            sortedWord = "".join(sorted(word))

            # If key exists, append word to the corresponding list
            if sortedWord in mappingDictionary:
                mappingDictionary[sortedWord].append(word)
            # Otherwise, create a new list for this key
            else:
                mappingDictionary[sortedWord] = [word]

        # Return all grouped anagrams as a list of lists
        return list(mappingDictionary.values())


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    # Input array of strings
    input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # Create Solution object
    solution = Solution()

    # Get grouped anagrams and print
    grouped_anagrams = solution.groupAnagrams(input_strings)
    print("Grouped Anagrams:", grouped_anagrams)
