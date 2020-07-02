class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer of 0, 2 's boundary and current element
        left, cur, right = 0, 0, len(nums) - 1

        while cur<right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
                left += 1
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1
            else:
                cur += 1




so = Solution()
print(so.sortColors([2,0,2,1,1,0]))