# https://www.youtube.com/watch?v=cyGTFYJZY_E&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=4
# 1 Recursion
import copy
class Solution:
    def subsets(self, nums: [int]) -> [[int]]:

        output = [[]]
        for num in nums:
            temp = []
            for curr in output:
                temp.append(curr + [num])
                # print(num)
                # print(temp)
            output += temp
            # output += [curr + [num] for curr in output]

        return output

so = Solution()
arr = [1,2,3]
print(so.subsets(arr))
arr.extend([4])
# print([]+[2], arr)

# 2 Back tracking
class Solution2:
    def subsets(self, nums: [int]) -> [[int]]:
        def backtrack(first=0, curr=[]):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

so2 = Solution2()
arr = [1, 2,2]
# print(arr[:])
# print(so2.subsets(arr))

class Solution3:
    def subsets(self, nums: [int]) -> [[int]]:
        self.result = [[],]
        item = [[]]


        # result.append(item)
        self.backtrack(0,nums,self.result,item)

        return self.result

    def backtrack(self, first, nums, result, item):
        if first >= len(nums):
            return
        item[0].append(nums[first])
        """In Python, we need to use deep copy, otherwise, the value will change as item change"""
        temp = copy.deepcopy(item[0])
        if temp not in result:
            result.append(copy.deepcopy(item[0]))
        # result += item
        self.backtrack(first + 1, nums, result, item)
        item[0].pop()
        self.backtrack(first + 1, nums, result, item)


so3 = Solution3()
print(so3.subsets(arr))

#

# 4 bit operation
# https://www.youtube.com/watch?v=cyGTFYJZY_E&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=5&t=1210s
class Solution4:
    def subsets(self, nums: [int]) -> [[int]]:
        result = []
        all_sets = 1 << len(nums)
        for i in range(all_sets):
            item = []
            for j in range(len(nums)):
                if i&(1<<j):
                    item.append(nums[j])
            result.append(item)

        return result

so4 = Solution4()
print(so4.subsets(arr))