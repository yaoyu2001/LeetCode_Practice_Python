# A string S of lowercase English letters is given.
# We want to partition this string into as many parts as possible so that each letter appears in at most one part,
# and return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# https://www.youtube.com/watch?v=s-1W5FDJ0lw&t=341s

class Solution:
    def partitionLabels(self, S: str) -> [int]:
        # First we find the last index of every letters
        last = {c:i for i,c in enumerate(S)}
        print(last)
        anchor, end = 0, 0
        ans = []
        # One greedy loop, find the "last" index where char in S occurs

        for i in range(len(S)):
            # Update the index of "end" when a letter's
            end = max(end, last[S[i]])
            if i == end:
                ans.append(end - anchor + 1)
                anchor = i + 1

        return ans


so = Solution()
print(so.partitionLabels("ababcbacadefegdehijhklij"))

