class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        self.word_dic = set(wordDict)
        self.memo = {}

        def helper(s):
            if s in self.memo:
                return self.memo[s]
            if s in self.word_dic:
                self.memo[s] = True
                return self.memo[s]

            for i in range(1, len(s)):
                left = s[0:i]
                right = s[i:]
                if right in self.word_dic and helper(left):
                    self.memo[s] = True
                    return self.memo[s]
            self.memo[s] = False
            return False

        return helper(s)

so = Solution()
print(so.wordBreak("cats", ["cats", "dog", "sand", "and", "cat"]))