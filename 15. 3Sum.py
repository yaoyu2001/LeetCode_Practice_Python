# https://www.youtube.com/watch?v=-AMHUdZc9ss

class Solution:
    def threeSum(self, nums: [int]) ->[[int]]:
        results = []
        nums.sort()
        print(nums)

        for i in range(0, len(nums) - 2):
            """Ignore duplicate number"""
            if i == 0 or nums[i] > nums[i - 1]:
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    if nums[i] + nums[start] + nums[end] == 0:
                        temp = [nums[i], nums[start], nums[end]]
                        results.append(temp)
                        while start < end and nums[start] == nums[start + 1]:  # [6]
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:  # [6]
                            end -= 1
                    """If sum < 0 means we need to find a bigger number"""
                    if nums[i] + nums[start] + nums[end] < 0:
                        """We use a temp variable to find the nearest different number"""

                        start += 1
                    elif nums[i] + nums[start] + nums[end] > 0:
                        """Same method if sum > 0 then, find a smaller number"""

                        end -= 1
                    else:
                        """Go on finding next appropriate number"""
                        start += 1
                        end -= 1
        return results



# nums = [-1, 0, 1, 2, -1, -4, 3]
nums = [-2,-2,0,0,2,2]
s = Solution

print(s.threeSum(None,nums))


# Here is a wrong solution. Why got wrong, just because when nums[0] + nums[1] + nums[2] == 0,
# and the arr is  [-2,-2,0,0,2,2] now i = 0 start = 2 end = 5. But the pointer just go forward one time.
# So Next loop, i = 0 start = 3 end = 4, also meet the conditions, then produce a duplicate answer.[-2,0,2]
# To correct it, we need to Eliminate every duplicate value when appending a list.
#
class Solution_wrong:
    def threeSum(self, nums: [int]) -> [[int]]:
        results = []
        nums.sort()
        print(nums)
        if len(nums) < 3:
            return
        elif len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                temp = []
                for i in nums:
                    temp.append(i)
                results.append(temp)
                return results
            else:
                return
        else:
            for i in range(0, len(nums) - 3):
                """Ignore duplicate number"""
                if i == 0 or nums[i] > nums[i - 1]:
                    start = i + 1
                    end = len(nums) - 1
                    while start < end:
                        if nums[i] + nums[start] + nums[end] == 0:
                            results.append([nums[i], nums[start], nums[end]])
                        """If sum < 0 means we need to find a bigger number"""
                        if nums[i] + nums[start] + nums[end] < 0:
                            """We use a temp variable to find the nearest different number"""
                            current_start = start
                            while nums[start] == nums[current_start] and start < end:
                                start += 1
                        elif nums[i] + nums[start] + nums[end] > 0:
                            """Same method if sum > 0 then, find a smaller number"""
                            current_end = end
                            while nums[end] == nums[current_end] and start < end:
                                end -= 1
                        else:
                            """Go on finding next appropriate number"""
                            start += 1
                            end -=1
        return results

sr = Solution_wrong()
print(sr.threeSum(nums))