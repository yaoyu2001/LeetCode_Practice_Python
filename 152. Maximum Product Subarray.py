# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# By intuition, it is a dynamic process question.
# Brute Force method will definite TLE
# So we can use DP, consider 3 situations: positive number, zero and negative number
# Just because the product of two negative numbers will be a positive number, so beside a variable to store
# the_max_so far, we also need another variable to store the_mix so far. To make sure that if current number is negative,
# We need to let the min_so_far to multiply current to get "the max_so_far"
# Eg. In array [-2, 3, -4, 0] (-2, 3, -4) will be the subarray which have max product
# So to get max_so_far and min_so_far we need to consider 3 situations too. max_so_far * current, min_so_far * current and current number

class Solution:
    def maxProduct(self, nums: [int]) -> int:
        # First consider boundary if input an empty array then return 0
        if len(nums) == 0:
            return 0

        # Declare 2 variables to store max and min value so far, in inital staus, if will be the first number in array
        max_so_far, min_so_far = nums[0], nums[0]
        # Result will be it if there only one element in array
        res = max_so_far

        # Begin to iterate, to get max and min value so far just because we have declared max and min from nums[0] so from nums[1]
        for i in range(1, len(nums)):
            curr = nums[i]
            # Use a temp variable to store max value so far or it will disturb the min value
            temp_max = max(max_so_far * curr, curr, min_so_far * curr)
            min_so_far = min(max_so_far * curr, curr, min_so_far * curr)
            # Update max value so far
            max_so_far = temp_max
            # Update result
            res = max(max_so_far, res)

        return res
