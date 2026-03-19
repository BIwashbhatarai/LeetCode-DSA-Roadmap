class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currentSum = 0
        hashMap = {0: 1}  # prefix sum 0 appeared once

        for num in nums:
            currentSum += num

            # If there is a prefix sum that is currentSum - k,
            # it means there is a subarray ending here with sum = k
            if currentSum - k in hashMap:
                count += hashMap[currentSum - k]

            # Update the hashmap with current prefix sum
            hashMap[currentSum] = hashMap.get(currentSum, 0) + 1

        return count


# Example usage
if __name__ == "__main__":
    obj = Solution()
    print(obj.subarraySum([1, 1, 1], 2))  # Output: 2
