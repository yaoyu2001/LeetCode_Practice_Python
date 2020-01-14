import collections
#https://www.youtube.com/watch?v=LupZFfCCbAU

# Optimized brute force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            seen = collections.defaultdict(int)
            j = i
            while j<n and seen[s[j]] != 1:
                seen[s[j]] = 1
                j +=1

            ans = max(ans, j - i)

        return ans

s1 = "abcabcbb"
s2 = "bbbbb"

s = Solution()

print(s.lengthOfLongestSubstring(s1))
print(s.lengthOfLongestSubstring(s2))

# HashTable and Sliding Window
# Window (i,j) with unique characters
# 1. Use a hashtable to store the last indies of each characters
# 2. Keep track the valid starting point
#   a. When there is a match update the starting point to the current one
# i = max(i, m[s[j]] + 1), len = j - i + 1

# idx = collections.defaultdict(lambda :-1)
# print(idx["a"])
def lengthOfLongestSubstring2(s: str) -> int:
    n = len(s)
    ans = 0
    idx = collections.defaultdict(lambda :-1)
    i = 0
    for j in range(n):
        i = max(i, idx[s[j]] + 1)
        ans = max(ans, j - i + 1)
        idx[s[j]] = j

    return ans

print(lengthOfLongestSubstring2(s1))
print(lengthOfLongestSubstring2(s2))