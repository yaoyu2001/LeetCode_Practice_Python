class Solution:
    def trap(self, height: [int]) -> int:
        left,right = 0, len(height)-1
        ans = 0

        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right])


                right -= 1

        return ans

so = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(so.trap(height))