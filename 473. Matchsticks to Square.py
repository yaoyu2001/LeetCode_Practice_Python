#https://www.youtube.com/watch?v=GL1HvaYKE40&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=10&t=9962s
import collections
class Solution:
    def makesquare(self, nums: [int]) -> bool:
        if len(nums) < 4:
            return False
        sum_num = sum(nums)
        if sum_num % 4 != 0:
            return False
        nums.sort(reverse=True)
        print(nums)
        self.bucket = collections.defaultdict(int)
        return self.generate(0, nums, sum_num//4, self.bucket )

    def generate(self, i, nums, target, bucket):
        if i >= len(nums):  # Use all of matches, return
            return self.bucket[0] == target and self.bucket[1] == target and self.bucket[2] == target and self.bucket[3] == target

        for j in range(4):
            if self.bucket[j] + nums[i] <= target:

                self.bucket[j] += nums[i]
                if self.generate(i+1, nums, target, self.bucket):
                    return True
                self.bucket[j] -= nums[i]  # cant put current match in current bucket, so we need to track back
        return False





so = Solution()
nums = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]

print(so.makesquare(nums))
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square
        if not nums:
            return False

        # Number of matchsticks we have
        L = len(nums)

        # Perimeter of our square (if one can be formed)
        perimeter = sum(nums)

        # Possible side of our square.
        possible_side =  perimeter // 4

        # If the perimeter can be equally split into 4 parts (and hence 4 sides, then we move on).
        if possible_side * 4 != perimeter:
            return False

        # Reverse sort the matchsticks because we want to consider the biggest one first.
        nums.sort(reverse=True)

        # This array represents the 4 sides and their current lengths
        sums = [0 for _ in range(4)]

        # Our recursive dfs function.
        def dfs(index):

            # If we reach the end of matchsticks array, we check if the square was formed or not
            if index == L:
                # If 3 equal sides were formed, 4th will be the same as these three and answer should be True in that case.
                return sums[0] == sums[1] == sums[2] == possible_side

            # The current matchstick can belong to any of the 4 sides (provided their remaining lenghts are >= the size of the current matchstick)
            for i in range(4):
                # If this matchstick can fir in the space left for the current side
                if sums[i] + nums[index] <= possible_side:
                    # Recurse
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    # Revert the effects of recursion because we no longer need them for other recursions.
                    sums[i] -= nums[index]
            return False
        return dfs(0)

# print(1<<8)

# byte calculate
class Solution3:
    def makesquare(self, nums):
        if len(nums) < 4:
            return False
        sum_num = sum(nums)
        if sum_num % 4 != 0:
            return False
        target = sum_num/4

        ok_subst = []  # All sides that fulfill condition
        ok_half = []   # All two sides that fulfill condition

        all = 1<<len(nums)

        for i in range(all):
            sum_temp = 0
            for j in range(len(nums)):
                if i&(1<<j):
                    sum_temp += nums[j]
            if sum_temp == target:
                ok_subst.append(i)

        for i in range(len(ok_subst)):
            for j in range(i+1,len(ok_subst)):
                if ok_subst[i] & ok_subst[j] == 0:
                    ok_half.append(ok_subst[i] | ok_subst[j])

        for i in range(len(ok_half)):
            for j in range(i+1,len(ok_subst)):
                if ok_half[i] & ok_half[j] == 0:
                    return True
        return False

so3 = Solution3()
print(so3.makesquare([1,1,2,2,2]))
print(so3.makesquare(nums))

            



