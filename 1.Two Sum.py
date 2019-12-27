class Solution:
    def twoSum(self,nums,target):
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = i
        # print(map.__contains__(1))
        for i in range(len(nums)):
            complement = target - nums[i]
            if map.__contains__(complement) and map[complement] != i:
                res = [i, map[complement]]
                return res
            print("No two sum solution")
        return

nums= [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums,target))