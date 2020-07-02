class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        sum_arr = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            sum_arr = max(nums[i], sum_arr + nums[i])
            res = max(sum_arr, res)
        return res
