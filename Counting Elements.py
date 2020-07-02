import collections
class Solution:
    def countElements(self, arr: [int]) -> int:
        map_arr = collections.Counter(arr)
        res = 0
        for item in arr:
            if item + 1 in map_arr:
                res += 1
                map_arr[item + 1] -= 1
                if map_arr[item + 1] == 0:
                    del map_arr[item + 1]
        return res

arr = [1, 2, 3]

so = Solution()
print(so.countElements(arr))

map1 = {"a":1, "b": 2}

for item in "abb":
    if item in map1:
        print(f"Before minus {map1}")
        map1[item] -= 1
        print(f"After minus {map1}")
        if map1[item] == 0:
            del map1[item]
        print(f"After del {map1}")