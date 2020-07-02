class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * (len(nums) + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[len(nums) - 1]
