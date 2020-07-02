class Solution:
    def largestDivisibleSubset(self, nums: [int]) -> [int]:
        if len(nums) == 0:
            return []
        dic = {}
        nums.sort()

        def EDS(i):
            if i in dic:
                return dic[i]
            tail = nums[i]
            max_Subset = []
            for j in range(0, i):
                if tail % nums[j] == 0:
                    sub_set = EDS(j)
                    max_Subset = max(max_Subset, sub_set, key=len)

            max_Subset = max_Subset.copy()
            max_Subset.append(tail)

            dic[i] = max_Subset
            return max_Subset

        return max([EDS(i) for i in range(len(nums))], key=len)
