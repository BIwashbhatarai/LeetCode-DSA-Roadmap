# Next Greater Element I – Brute Force Approach
# LeetCode #496
# This solution uses brute-force method to find the first greater element to the right.


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        Finds the next greater element for each element in nums1 from nums2.

        :type nums1: List[int]  # Subset array
        :type nums2: List[int]  # Full array
        :rtype: List[int]       # List of next greater elements
        """
        result = []  # List to store next greater elements

        # Loop over each number in nums1
        for num in nums1:
            nextGreaterElement = -1  # Default if no greater element found
            # Find index of num in nums2
            index = nums2.index(num)

            # Loop through elements to the right in nums2
            for nextEl in nums2[index + 1 :]:
                if nextEl > num:
                    nextGreaterElement = nextEl
                    break  # Stop at the first greater element

            result.append(nextGreaterElement)

        return result


# Example usage
if __name__ == "__main__":
    obj = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print("Next Greater Elements:", obj.nextGreaterElement(nums1, nums2))
    # Output: [ -1, 3, -1 ]
