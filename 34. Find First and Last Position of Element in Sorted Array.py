class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        return [self.left_bound(nums, target), self.right_bound(nums, target)]

    def left_bound(self, nums: [int], target: int):
        begin = 0
        end = len(nums) - 1

        while begin <= end:

            mid = (begin + end) // 2
            if target == nums[mid]:
                if mid == 0 or target > nums[mid-1]:
                    return mid
                end = mid - 1
            elif target > nums[mid]:
                begin = mid + 1
            elif target < nums[mid]:
                end = mid - 1

        return -1

    def right_bound(self, nums: [int], target: int):

        begin = 0
        end = len(nums) - 1

        while begin <= end:

            mid = (begin + end) // 2
            if target == nums[mid]:
                if mid == len(nums) - 1 or target < nums[mid+1]:
                    return mid
                begin = mid + 1
            elif target > nums[mid]:
                begin = mid + 1
            elif target < nums[mid]:
                end = mid - 1

        return -1

so = Solution()

arr = [3,4,5,8,8,8,8,8,8,10]
arr2 = [2,2,2]
print(so.left_bound(arr,8))
print(so.right_bound(arr,8))

print(so.searchRange(arr2,2))
