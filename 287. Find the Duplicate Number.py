class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        # Use two pointers fast and slow
        # first round find point of intersection
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Start to loop begin is a, and loop begin to intersection is b
        # Intersection is c
        # So 2*(a+b) = a + b + c + b
        # So a = s that is begin to loop start point equal to intersection to loop start

        # Let slow back to start
        slow = nums[0]
        while slow!= fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

arr = [3,1,3,4,2]
so = Solution()
print(so.findDuplicate(arr))

