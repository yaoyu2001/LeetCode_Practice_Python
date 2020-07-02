import collections
# 2020.4.22 Lc
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        count = 0
        sum_ = 0

        self.map_ = collections.defaultdict(int)

        self.map_[0] = 1
        for i in nums:
            sum_ += i
            if self.map_.__contains__(sum_ - k):
                count += self.map_.get(sum_ - k)
            self.map_[sum_] = self.map_.get(sum_, 0) + 1

        return count

so = Solution()
nums = [3, 4, 7, 2, -3, 1, 7, -7, 7]
nums2 = [1, 1, -1, 1, 1,  4]
print(so.subarraySum(nums, 7))
print(so.map_)
print(so.subarraySum(nums2, 5))
print(so.map_)