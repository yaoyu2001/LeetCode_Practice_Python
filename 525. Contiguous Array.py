class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        prefix_sums = {}  # A Hashtable to track the first index of each prefix sum appears
        ans = 0
        sum = 0
        for i, num in enumerate(nums):
            if num == 1:
                sum += 1
            else:
                sum -= 1
            if sum == 0:
                ans = i + 1
            elif sum in prefix_sums:
                ans = max(ans, i - prefix_sums[sum])
            else:
                prefix_sums[sum] = i
        return ans


