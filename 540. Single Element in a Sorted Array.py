class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        low,high = 0,len(nums)-1

        while low<high:
            mid = low + (high-low)//2
            right_part_even = (high - mid)%2 == 0
            if nums[mid] == nums[mid+1]:
                if right_part_even:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid-1]:
                if right_part_even:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[low]



input1 = [1,1,2,3,3,4,4,8,8]
input2 = [3,3,7,7,10,11,11]
so = Solution()
print(so.singleNonDuplicate(input1))
print(so.singleNonDuplicate(input2))