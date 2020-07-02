class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:

        begin = 0
        end = len(nums)

        while begin<=end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return begin

