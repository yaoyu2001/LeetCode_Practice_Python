import copy
class Solution:
    def subsetsWithDup(self, nums: [int], target) -> [[int]]:

        self.result = [[], ]
        item = []
        sum_target = 0

        nums.sort()
        # result.append(item)
        self.backtrack(0, nums, self.result, item,sum_target,target)

        return self.result

    def backtrack(self, first, nums, result, item,sum_target,target):
        if first >= len(nums) or sum_target > target:
            return
        # for i in item:
        #     for n in i:
        #         sum_target += n
        #         if sum_target > 4:
        #             return
        item.append(nums[first])
        sum_target += nums[first]
        """In Python, we need to use deep copy, otherwise, the value will change as item change"""
        temp = copy.deepcopy(item)
        sum_result = 0
        # for j in temp:
        #     sum_result += j
        if temp not in result and sum_target==target:
            result.append(copy.deepcopy(item))
        # result += item
        self.backtrack(first + 1, nums, result, item,sum_target,target)
        sum_target -= nums[first]
        item.pop()
        self.backtrack(first + 1, nums, result, item,sum_target,target)

so = Solution()

arr = [10,1,2,7,6,1,5]

print(so.subsetsWithDup(arr,8))