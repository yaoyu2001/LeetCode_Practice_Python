import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_t = collections.Counter(t)
        map_s = collections.defaultdict(int)
        vec_t = []
        for item in t:
            vec_t.append(item)

        begin = 0
        result = ""

        for i in range(len(s)):
            """Start iterate"""
            map_s[s[i]] += 1
            while begin < i:
                begin_char = s[begin]
                if map_t[begin_char] == 0:  #
                    begin += 1
                elif map_s[begin_char] > map_t[begin_char]:
                    map_s[s[begin]] -= 1
                    begin += 1

                else:
                    break
            if self.check_window(map_s, map_t, vec_t):
                new_window_len = i - begin + 1
                if result =="" or len(result) > new_window_len:
                    result = s[begin: begin + new_window_len]
        return result

    def check_window(self, map_s, map_t, vec_t):
        for i in range(len(vec_t)):
            if map_s[vec_t[i]] < map_t[vec_t[i]]:
                return False
        return True

so = Solution()

print(so.minWindow("ADOBECODEBANC", "ABC"))

dic = {"a":1,"b":2}
dic["b"] -= 1

print(dic)

class Solution2:
    def minWindow(self, s, t):


        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = collections.Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]