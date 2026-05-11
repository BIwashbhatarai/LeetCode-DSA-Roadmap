class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        mapping_Dictionary = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in mapping_Dictionary:
                mapping_Dictionary[sorted_word].append(word)
            else:
                mapping_Dictionary[sorted_word] = [word]

        return list(mapping_Dictionary.values())


obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
