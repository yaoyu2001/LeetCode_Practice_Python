import collections


class Solution:
    def wordPattern(self, pattern, str):

        t = str.split()
        index_s = collections.defaultdict(int)
        index_t = collections.defaultdict(int)
        if len(pattern) != len(t):
            return False

        for i in range(len(pattern)):
            if index_s[pattern[i]] == 0:
                index_s[pattern[i]] = i + 1

            if index_t[t[i]] == 0:
                index_t[t[i]] = i + 1

            if index_s[pattern[i]] != index_t[t[i]]:
                return False

        return True

# Method 2
# https://www.youtube.com/watch?v=u3fnbw7Ut7g&list=PLJCHnHCd1EzRBdOdjbPxxQK75OJswMXjY&index=9&t=4768s
class Solution2:
    def wordPattern(self, pattern, str):

        word_map = {}  # str-> pattern map
        used = set()

        t = str.split()
        pos = 0  # current position

        if len(pattern) != len(t):
            return False

        for i in range(len(t)):
            word = t[i]
            if not word_map.__contains__(word):
                if used.__contains__(pattern[i]): # If a new word appeared but corresponding pattern word has been used
                    return False
                word_map[word] = pattern[i]
                used.add(pattern[i])
            else:
                if word_map[word] != pattern[pos]:  # Current word not match word in pattern
                    return False

        return True
