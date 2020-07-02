import collections


# https://www.youtube.com/watch?v=LupZFfCCbAU

# Optimized brute force
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            seen = collections.defaultdict(int)
            j = i
            while j < n and seen[s[j]] != 1:
                seen[s[j]] = 1
                j += 1

            ans = max(ans, j - i)

        return ans


s1 = "abcabcdbb"
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
    idx = collections.defaultdict(lambda: -1)
    begin = 0
    for j in range(n):
        begin = max(begin, idx[s[j]] + 1)
        ans = max(ans, j - begin + 1)
        idx[s[j]] = j

    return ans


print(lengthOfLongestSubstring2(s1))
print(lengthOfLongestSubstring2(s2))


# Method 3 https://www.youtube.com/watch?v=u3fnbw7Ut7g&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=9&t=7849s
# Slide window same as method 2

def lengthOfLongestSubstring(s):
    begin = 0  # Head pointer of window
    result = 0  # Maximal length

    word = ""
    char_map = collections.defaultdict(int)

    for i in range(len(s)):
        char_map[s[i]] += 1
        if char_map[s[i]] == 1:
            word += s[i]
            result = max(result, len(word))

        else:
            while begin < i and char_map[s[i]] > 1:
                char_map[s[begin]] -= 1
                begin += 1

            word = ""  # Update word
            for j in range(begin, i + 1):
                word += s[j]

    return result
