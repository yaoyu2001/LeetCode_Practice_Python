import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        print(counts.get())
        return max(counts.keys(), key=counts.get)
