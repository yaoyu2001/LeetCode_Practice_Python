class Solution:
    def search(self, nums: [int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if nums[begin] < nums[mid]:  # Means begin to mid - 1 is an increasing range; mid+1 to end is a rotation range
                    if target >= nums[begin]:  # Means we can find target in increasing range.
                        end = mid - 1
                    else:  # target < nums[begin], so we need to find it in rotation range.
                        begin = mid + 1
                elif nums[begin] > nums[mid]: # Means begin to mid - 1 is a rotation range; mid+1 to end is an increasing range
                    end = mid - 1  # Because in this case target < nums[mid], we only need to find target in rotation range
                elif nums[begin] == nums[mid]: # In this case, the array only have two elements, begin == mid and target < nums[mid]. So target will equal to nums[end]
                    begin = mid + 1
            elif target > nums[mid]:
                if nums[begin] < nums[mid]:  # Means begin to mid - 1 is an increasing range; mid+1 to end is a rotation range
                    begin = mid + 1   # Only need to find target in rotation range
                elif nums[begin] > nums[mid]: # Means begin to mid - 1 is a rotation range; mid+1 to end is an increasing range
                    if target >= nums[begin]:  # Means we can find target in rotation range.
                        end = mid - 1
                    else:  # In this case, because begin to mid - 1 is an increasing range, and target > nums[mid] we only need to find element in rotation range
                        begin = mid + 1
                elif nums[begin] == nums[mid]:  # In this case, the array only have two elements, begin == mid and target < nums[mid]. So target will equal to nums[end]
                        begin = mid + 1
        return -1

so = Solution()
arr = [15,20,1,3,6,7,9,12]
arr2 = [6,7]
print(so.search(arr2, 6))