class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)

        def dsf(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    return True
                if prefix in d and dsf(suffix):
                    return True
            return False

        res = []

        for word in words:
            if dsf(word):
                res.append(word)
        return res

input_= ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

so = Solution()
print(so.findAllConcatenatedWordsInADict(input_))