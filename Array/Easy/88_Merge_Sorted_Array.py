class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# Example usage:
if __name__ == "__main__":
    obj = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [4, 5, 6]
    obj.merge(nums1, 3, nums2, 3)
    print(nums1)  # Output: [1, 2, 3, 4, 5, 6]
